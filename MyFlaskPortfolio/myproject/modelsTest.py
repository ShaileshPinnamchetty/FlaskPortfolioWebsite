from myproject import db
from myproject.models import Message

#print all the rows
# messages = Message.query.all()
# print (messages)

#delete all the rows
all = Message.query.delete()
print(all)
# db.session.delete(all)
db.session.commit()