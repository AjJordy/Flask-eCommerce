# Flask-eCommerce

- Virtual env: `python -m venv venv` 
- Enter on Vitual env: `source venv/bin/activate`
- Install dependences: `pip3 -r install requirements.txt`
- Init database: 

```python
# $ flask shell
db.drop_all()
db.create_all()
db.session.commit()
exit()
```

## AWS Elastic Beanstalk

```bash
eb init -p python-3.11 api-dev --region us-east-1
eb create api-dev
eb deploy api-dev
eb open api-dev
eb terminate api-dev
```