# Flask-eCommerce

- Virtual env: `python -m venv venv` 
- Enter on Vitual env: `source venv/bin/activate`
- Install dependences: `pip3 -r install requirements.txt`
- Init database: 

```python
# $ flask shell
db.create_all()
db.session.commit()
exit()

# $ flask shell
db.drop_all()
db.create_all()
db.session.commit()
exit()
```
