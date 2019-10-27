### Creating a polling question example
./manage shell
from polls.models import Choice, Question
from django.utils import timezone
 q = Question(question_text="Cats or Dogs?", pub_date=timezone.now())
 q.save()
 q.choice_set.create(choice_text='Cats!', votes=0)
 q.choice_set.create(choice_text='Dogs!', votes=0)
exit()
