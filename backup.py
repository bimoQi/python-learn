#!/usr/bin/env python3
# coding: utf-8

# 需要安装 pymysql
# sudo apt-get install python3-pip
# sudo pip3 install pymysql
# 安装sudo apt-get install percona-xtrabackup

import os
import subprocess
import pymysql
import warnings


class Restore(object):
    def __init__(self, sql_name, mysql_user='root', mysql_passwd='root', edusoho_name=''):
        self.sql_name = sql_name
        self.mysql_user = mysql_user
        self.mysql_passwd = mysql_passwd
        self.edusoho_name = edusoho_name

    def start_restore(self):
        output = os.popen('file ' + self.sql_name)
        isTarType = output.read().split(',')[1].find('from Unix')
        if os.path.isfile(self.sql_name):
            if isTarType != -1:
                self._xtrabackup_restore()
            else:
                self._mysql_restore()
        else:
            self.echo_style('%s 不是文件!' % self.sql_name, 'error')
            return
        if self.edusoho_name:
            self.echo_style('正在创建edusoho目录', 'green')
            p = subprocess.Popen(['rm -rf /var/www/edusoho_restore_test; mkdir /var/www/edusoho_restore_test'],shell=True)
            p.communicate()
            p = subprocess.Popen(['tar -zxf ' + self.edusoho_name + ' -C /var/www/edusoho_restore_test/; chmod -R 777 /var/www/edusoho_restore_test/'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, err = p.communicate()
            if p.returncode != 0:
                self.echo_style(err.decode('utf-8'), 'error')
                return
            file = open('/etc/nginx/sites-enabled/edusoho-backup-test', 'w+')
            file.write(self.nginx_conf());
            file.close()
            p = subprocess.Popen(['sudo service nginx reload'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, err = p.communicate()
            if p.returncode != 0:
                self.echo_style(err.decode('utf-8'), 'error')
                return
            if isTarType == -1:
                p = subprocess.Popen(["sed -i '5s/^.*$/    database_name: edusoho_restore_test/' /var/www/edusoho_restore_test/edusoho/app/config/parameters.yml;" +
                    "sed -i '6s/^.*$/    database_user: "+self.mysql_user+"/' /var/www/edusoho_restore_test/edusoho/app/config/parameters.yml;" +
                    "sed -i '7s/^.*$/    database_password: "+self.mysql_passwd+"/' /var/www/edusoho_restore_test/edusoho/app/config/parameters.yml;"],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                output, err = p.communicate()
                if p.returncode != 0:
                    self.echo_style(err.decode('utf-8'), 'error')
                    return
            self.echo_style('恢复成功  请访问localhost:888', 'success')
            

    def nginx_conf(self):
        return '''
server {
        listen 888;

        server_name localhost;

        root /var/www/edusoho_restore_test/edusoho/web;

        access_log /var/log/nginx/edusoho-backup-test.access.log;
        error_log /var/log/nginx/edusoho-backup-test.error.log;

        location / {
            add_header X-Frame-Options SAMEORIGIN;
            index app_dev.php;
            try_files $uri @rewriteapp;
        }

        location @rewriteapp {
            rewrite ^(.*)$ /app_dev.php/$1 last;
        }

        location ~ ^/static-dist {
            if (-f $document_root/static-dist/dev.lock)
            {
                rewrite ^(.*)$ http://127.0.0.1:3030$1 last;
            }
        }

        location ~ ^/udisk {
            internal;
            root /var/www/edusoho_restore_test/edusoho/app/data/;
        }

        location ~ ^/(app|app_dev)\.php(/|$) {
            # [改] 请根据实际php-fpm运行的方式修改
        fastcgi_pass   unix:/var/run/php5-fpm.sock;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
            include fastcgi_params;
            fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;
            fastcgi_param  HTTPS              off;
            fastcgi_param HTTP_X-Sendfile-Type X-Accel-Redirect;
            fastcgi_param HTTP_X-Accel-Mapping /udisk=/var/www/edusoho/app/data/udisk;
            fastcgi_buffer_size 128k;
            fastcgi_buffers 8 128k;
            fastcgi_connect_timeout 300s;
            fastcgi_send_timeout 300s;
            fastcgi_read_timeout 300s;
        }

        location ~* \.(jpg|jpeg|gif|png|ico|swf)$ {
            expires 3y;
            access_log off;
            gzip off;
        }

        location ~* \.(css|js)$ {
            access_log off;
            expires 3y;
        }

        location ~ ^/files/.*\.(php|php5)$ {
            deny all;
        }

        location ~ \.php$ {
            # [改] 请根据实际php-fpm运行的方式修改
            fastcgi_split_path_info ^(.+\.php)(/.*)$;
            include fastcgi_params;
            fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;
            fastcgi_param  HTTPS              off;
        }
    }
        '''


    def _xtrabackup_restore(self):
        if os.path.isdir('/var/lib/mysql-backup'):
            self.echo_style('已经存在目录 "/var/lib/mysql-backup"  不能备份恢复! 请处理后再进行操作,可选择2进行还原', 'error')
            return
        self.echo_style('正在解压sql文件...', 'green')
        p = subprocess.Popen(['tar -zxf ' + self.sql_name], stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        if p.returncode != 0:
            self.echo_style(err.decode('utf-8'), 'error')
            return
        self.echo_style('正在备份原sqldata目录...', 'green')
        p = subprocess.Popen(['mv -f /var/lib/mysql /var/lib/mysql-backup; mkdir  /var/lib/mysql'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        if p.returncode != 0:
            self.echo_style(err.decode('utf-8'), 'error')
            return
        self.echo_style('正在关闭mysql...', 'green')
        p = subprocess.Popen(['sudo service mysql stop'],  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        p.communicate()
        self.echo_style('正在使用innobackupex进行数据恢复...', 'green')
        path = os.path.split(os.path.abspath(sql_name))[0]
        p = subprocess.Popen(['innobackupex', '--user=' + self.mysql_user, '--password=' + self.mysql_passwd, '--ibbackup=xtrabackup_55',
                              '--copy-back', path + '/edusoho-db-backup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        if p.returncode != 0:
            self.echo_style(err.decode('utf-8'), 'error')
            return
        p = subprocess.Popen(['chown', 'mysql:mysql', '/var/lib/mysql', '-Rf'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p = subprocess.Popen(
            ['rm -rf ' + path + '/edusoho-db-backup'], shell=True)
        self.echo_style('正在启动mysql...', 'green')
        p = subprocess.Popen(['sudo service mysql start'], stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        if p.returncode != 0:
            self.echo_style(err.decode('utf-8'), 'error')
            return
        self.echo_style('运行成功!', 'success')

    def _mysql_restore(self):
        self.echo_style('正在解压sql文件...', 'green')
        path = os.path.split(os.path.abspath(sql_name))[0]
        p = subprocess.Popen(['gunzip -c ' + self.sql_name + ' > ' + path + '/edusoho.sql'],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        if p.returncode != 0:
            self.echo_style(err.decode('utf-8'), 'error')
            return
        self.echo_style('正在创建数据库edusoho_restore_test...', 'green')
        conn = pymysql.connect(
            host='localhost', user=self.mysql_user, passwd=self.mysql_passwd, charset='utf8')
        cursor = conn.cursor()
        try:
            cursor.execute('drop database if exists edusoho_restore_test')
            cursor.execute('create database edusoho_restore_test')
        except Exception as e:
            pass
        cursor.close()
        conn.close()
        self.echo_style('正在恢复数据库...', 'green')
        p = subprocess.Popen(['mysql -u' + self.mysql_user + ' -p' + self.mysql_passwd + ' edusoho_restore_test < ' +
                              path + '/edusoho.sql'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, err = p.communicate()
        if p.returncode != 0:
            self.echo_style(err.decode('utf-8'), 'error')
            return
        os.system('rm ' + path + '/edusoho.sql')
        self.echo_style('运行成功!', 'success')

    def restore_back(self):
        if os.path.isdir('/var/lib/mysql-backup'):
            self.echo_style('正在关闭mysql...', 'green')
            p = subprocess.Popen(['sudo service mysql stop'],  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            p.communicate()
            self.echo_style('正在还原mysql data目录...', 'green')
            p = subprocess.Popen(['rm -rf /var/lib/mysql; mv /var/lib/mysql-backup /var/lib/mysql; chown mysql:mysql /var/lib/mysql/ -Rf'],
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, err = p.communicate()
            if p.returncode != 0:
                self.echo_style(err.decode('utf-8'), 'error')
                return
            self.echo_style('正在启动mysql...', 'green')
            p = subprocess.Popen(['sudo service mysql start'], stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, err = p.communicate()
            if p.returncode != 0:
                self.echo_style(err.decode('utf-8'), 'error')
                return
        else:
            try:
                conn = pymysql.connect(
                host='localhost', user=self.mysql_user, passwd=self.mysql_passwd, charset='utf8')
            except Exception as e:
                self.echo_style('mysql conn error: '+e.args[1], 'error')
                return
            cursor = conn.cursor()
            stat = cursor.execute('show databases;')
            stats = 0
            for a in cursor.fetchall():
                if a[0] == 'edusoho_restore_test':
                    stats = 1
            if stats == 1:
                cursor.execute('drop database edusoho_restore_test')
            else:
                self.echo_style('没有/var/lib/mysql-backup目录 也没有edusoho_restore_test数据库~.~', 'green')
            cursor.close()
            conn.close()
        p = subprocess.Popen(['rm -rf /var/www/edusoho_restore_test'], shell=True)
        p.communicate()
        self.echo_style('运行成功!', 'success')

    def echo_style(self, info, style):
        style_dict = {"red": "\033[31m", "green": "\033[32m", "error": "\033[37;41m", "success": "\033[37;42m"}
        print(style_dict[style],info,'\033[0m')

if __name__ == '__main__':
    if os.geteuid() != 0:
        print('\033[31m必须以root权限运行!\033[0m')
        os._exit(0)
    warnings.filterwarnings("ignore")
    mode = input("请输入   1.开始还原数据     2.一切恢复原样: ")
    if mode == '1':
        mysql_user = input('输入数据库帐号(默认root): ')
        mysql_passwd = input('输入数据库密码(默认root): ')
        if os.path.isdir('/var/lib/mysql-backup'):
            print('\033[31m已经存在目录 "/var/lib/mysql-backup"  不能备份恢复! 请处理后再进行操作,可选择2进行还原\033[0m')
            exit()
        sql_name = input('输入数据库压缩文件路径: ')
        edusoho_name = input('请输入edusoho压缩文件路径(可选): ')
        restore = Restore(sql_name, mysql_user if mysql_user !=
                          '' else 'root', mysql_passwd if mysql_passwd != '' else 'root', 
                          edusoho_name)
        restore.start_restore()
    elif mode == '2':
        mysql_user = input('输入数据库帐号(默认root): ')
        mysql_passwd = input('输入数据库密码(默认root): ')
        restore = Restore('', mysql_user if mysql_user != '' else 'root',
                          mysql_passwd if mysql_passwd != '' else 'root')
        restore.restore_back()
    else:
        print('\033[31m输入有误\033[0m')
        exit()
