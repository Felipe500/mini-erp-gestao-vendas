PROJECT_NAME=mini-erp-gestao-vendas/
DIR_BASE=/root/backend
BASE=/root/backend/$PROJECT_NAME

VENV=$DIR_BASE/env
echo "### PROJECT 1 1 ###"
echo "ENTER FOLDER PROJECT"
cd $BASE && . $VENV/bin/activate

echo "### Pip install ###"
poetry install

echo "### Django check ###"
python manage.py check --settings=config.settings.production

echo "### Migration ###"
python manage.py migrate --settings=config.settings.production

echo "### Sync with S3 ###"
python manage.py collectstatic --noinput
python manage.py collectstatic --noinput --settings=config.settings.production

echo  "### Restart gunicorn service and socket ###"
sudo systemctl daemon-reload
sudo systemctl restart gunicorn_portifolio.socket
sudo systemctl restart gunicorn_portifolio.service


echo "### Create symbolic link nginx config ###"
sudo ln -sfn /root/backend/mini-erp-gestao-vendas/nginx/backend.conf /etc/nginx/sites-enabled
if sudo nginx -t 2>&1 | grep -q 'successful'; then
    echo "### Reload Nginx ###"
    sudo /etc/init.d/nginx reload
else
    echo "Nginx Fail"
fi


