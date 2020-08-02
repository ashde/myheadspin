# Install WordPress on EC2 using RDS MySQL DB
yum update -y
amazon-linux-extras install -y php7.2 
yum install -y httpd
systemctl start httpd
systemctl enable httpd
cd /var/www/html
wget https://wordpress.org/latest.tar.gz 
tar -xzf latest.tar.gz
cp -r wordpress/* ./
chmod -R 755 wp-content
chown -R apache:apache wp-content
yum install php-mbstring -y
systemctl restart httpd
systemctl restart php-fpm
wget https://www.phpmyadmin.net/downloads/phpMyAdmin-latest-all-languages.tar.gz
mkdir phpMyAdmin && tar -xvzf phpMyAdmin-latest-all-languages.tar.gz -C phpMyAdmin --strip-components 1
rm phpMyAdmin-latest-all-languages.tar.gz