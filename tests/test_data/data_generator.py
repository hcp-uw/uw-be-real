from __future__ import annotations
# uuid
from uuid import uuid4
# time
from time import time
# random
from random import randint
from random import choice
# system
import os
import json

"""
WARNING: The code below is garb and should not be used in the actual app.
"""

# classes
class User:
    """This class defines a User in the _tgr app."""
    def __init__(self, 
            fullname: str, 
            username: str,
            email: str,
            phone: str,
            profile_icon: str,
            streak: int,
            streak_emoji: str,
            user_id: str = str(uuid4())) -> None:
        # set attributes
        self.details: dict = {
            'user_id': user_id,
            'fullname': fullname,
            'username': username,
            'profile_icon': profile_icon,
        }
        self.contacts: dict = {
            'email': email,
            'phone': phone,
        }
        self.streak: dict = {
            'days': streak,
            'emoji': streak_emoji,
        }
        self.friends: set[User] = set()

    def add_friends(self, *friends: User) -> None: 
        for friend in friends:
            if friend not in self.friends:
                self.friends.add(friend)
    
    def get_friends(self) -> list:
        return [friend.details for friend in self.friends]

    def get_user(self) -> dict:
        return {
            'details': self.details,
            'contacts': self.contacts,
            'streak': self.streak, 
            'friends': self.get_friends(),
        }
    
    def __dict__(self) -> dict:
        return self.get_user()
    
    def json_serialize(self) -> str:
        return json.dumps(self.get_user(),
            indent=4)

    def __repr__(self) -> str:
        return str({
            'user_details': self.details,
            'user_streak': self.streak, 
        })

class Post:
    """This class defines a Post in the _tgr app."""
    def __init__(self,
            author: User,
            front_image: str,
            back_image: str,
            caption: str,
            location: str,
            # timestamp is optional for this case, but should be generated on post creation
            timestamp: float = time()) -> None:
        # set attributes
        self.metadata: dict = {
            'post_id': str(uuid4()),
            'author': author,
            'location': location,
            'time_created': timestamp,
        }
        self.content: dict = {
            'front_image': front_image,
            'back_image': back_image,
            'caption': caption,
            'comments': CommentSection(self.metadata['post_id']),
        }
    
    def comments(self) -> CommentSection:
        return self.content['comments']
    
    def get_post(self) -> dict:
        return {
            'metadata': self.metadata,
            'content': self.content,
        }
    
    # def __dict__(self) -> dict:
    #     return self.get_post()
    
    def json_serialize(self) -> str:
        return json.dumps(self, 
            default=lambda o: o.__dict__,
            indent=4)

    def __repr__(self) -> str:
        return str({
            'metadata': self.metadata,
            'content': self.content,
        })


class CommentSection:
    """This class defines a comment section of a Post."""
    def __init__(self, post_id: str) -> None:
        self.metadata: dict = {
            'post_id': post_id,
            'comment_section_id': str(uuid4()),
        }
        self.content: dict = {
            'comments': [],
            'reactions': [],
        }

    def add_comment(self, comment: Comment) -> CommentSection:
        self.content['comments'].append(comment)
        return self
    
    def get_comments(self) -> list[Comment]:
        return self.content['comments']
    
    def add_reaction(self, reaction_icon: str) -> Comment:
        self.content['reactions'].append(reaction_icon)
        return self
    
    def get_comment_section(self) -> dict:
        return {
            'metadata': self.metadata,
            'content': self.content,
        }
    
    # def __dict__(self) -> dict:
    #     return self.get_comment_section()
    
    def json_serialize(self) -> str:
        return json.dumps(self, 
            default=lambda o: o.__dict__,
            indent=4)

    def __repr__(self) -> str:
        return str(self.content['comments'])


class Comment:
    """This class defines a comment in a CommentSection."""
    def __init__(self, 
            author: User,
            body: str,
            time_created: float = time()) -> Comment:
        # set attributes
        self.metadata: dict = {
            'author': author,
            'time_created': time_created,
        }
        self.content: dict = {
            'comment_body': body,
            # realistically, this would be a priority queue 
            'comment_replies': []
        }
        return self
    
    def add_reply(self, comment: Comment) -> Comment:
        self.content['comment_replies'].append(comment)
        return self

    def get_reply(self) -> Comment:
        return self.content['comment_replies']
    
    def get_comment(self) -> dict:
        return {
            'metadata': self.metadata,
            'content': self.content,
        }
    
    # def __dict__(self) -> dict:
    #     return self.get_comment()
    
    def json_serialize(self) -> str:
        return json.dumps(self, 
            default=lambda o: o.__dict__,
            indent=4)

    def __repr__(self) -> str:
        return str({
            'metadata': self.metadata,
            'content': self.content,
        })
    

# data gen
users = [
    # 0
    User(fullname = 'li, haosen', 
        username = 'hoeli', 
        email = 'hoeli@uw.edu', 
        phone = '206-023-1234',
        profile_icon = 'https://cdn.discordapp.com/avatars/706310789241241613/7eb79671837f009c9ca20a5de5899176.webp',
        streak = 4,
        streak_emoji = "😊"),
    # 1
    User(fullname = 'tran, peter', 
        username = 'Lil Pete', 
        email = 'lilpete@uw.edu', 
        phone = '206-123-1234',
        profile_icon = 'https://cdn.discordapp.com/avatars/233717632837222400/4913615b121b70ae259cd6d37c38b635.webp',
        streak = 14,
        streak_emoji = "🔥"),
    # 2
    User(fullname = 'ly, alan', 
        username = 'Alannnn', 
        email = 'alannnn@uw.edu', 
        phone = '206-223-1234',
        profile_icon = 'https://cdn.discordapp.com/avatars/220355980246908929/66abe18f3f18b78600ff8fe6719d2b9f.webp',
        streak = 24,
        streak_emoji = "😊"),
    # 3
    User(fullname = 'dang, hai', 
        username = 'haidef', 
        email = 'haidef@uw.edu', 
        phone = '206-323-1234',
        profile_icon = 'https://cdn.discordapp.com/avatars/216028595380813825/b868936dcb1197b4f2f036b660ffc031.webp',
        streak = 43,
        streak_emoji = "🔥"),
    # 4
    User(fullname = 'kim, andrew', 
        username = 'minsung', 
        email = 'minsung@uw.edu', 
        phone = '206-423-1234',
        profile_icon = 'https://cdn.discordapp.com/avatars/564634987270242354/0ef0008a19bec8c33336448e066b67fc.webp',
        streak = 4,
        streak_emoji = "😊"),
    # 5
    User(fullname = 'tran, steven', 
        username = 'SchmoopTheGuy', 
        email = 'schmooptheguy@uw.edu', 
        phone = '206-523-1234',
        profile_icon = 'https://cdn.discordapp.com/avatars/232655252799619072/ce5896316b9956f2ebbb8ff7fbbfe48f.webp',
        streak = 2,
        streak_emoji = "🔥"),
    # 6
    User(fullname = 'le, anthony', 
        username = 'xorxer', 
        email = 'xorxer@uw.edu', 
        phone = '206-623-1234',
        profile_icon = 'https://cdn.discordapp.com/avatars/212774023912882177/00b043d84edfcc273a0006e7bf8c27f2.webp',
        streak = 6,
        streak_emoji = "😊"),
]

random_strings = [
    'Normal activities took extraordinary amounts of concentration at the high altitude.',
    'In the end, he realized he could see sound and hear words.',
    'This made him feel like an old-style rootbeer float smells.',
    'There were white out conditions in the town; subsequently, the roads were impassable.',
    'Writing a list of random sentences is harder than I initially thought it would be.',
    'Nobody has encountered an explosive daisy and lived to tell the tale.',
    'He found rain fascinating yet unpleasant.',
    'The father handed each child a roadmap at the beginning of the 2-day road trip and explained it was so they could find their way home.',
    'The lyrics of the song sounded like fingernails on a chalkboard.',
    'Twin 4-month-olds slept in the shade of the palm tree while the mother tanned in the sun.',
    'He went back to the video to see what had been recorded and was shocked at what he saw.',
    'I love eating toasted cheese and tuna sandwiches.',
    'Facing his greatest fear, he ate his first marshmallow.',
    'The door slammed on the watermelon.',
    'He excelled at firing people nicely.',
]

random_locations = [
    'Seattle',
    'Bothell',
    'Tacoma',
    'Vancouver',
    'Lynnwood',
    'Idk Somewhere Else'
]

posts = [
    Post(author = users[0],
         front_image = 'https://media.istockphoto.com/id/1129084458/photo/real-chinese-young-man-with-very-excited-expression-and-closed-eyes.jpg?s=612x612&w=0&k=20&c=ghZ6gG4oJr0PWvsKU3Gac7xacyj4-OnAjUB375M9T0I=',
         back_image = 'https://images.unsplash.com/photo-1571623922473-9e12bba94feb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fHNlYXR0bGV8ZW58MHwxfDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
         caption = choice(random_strings),
         location = choice(random_locations)),
    Post(author = users[1],
         front_image = 'https://media.istockphoto.com/id/1143002137/photo/portrait-of-real-chinese-man-with-furious-expression.jpg?s=612x612&w=0&k=20&c=5fPRJiwy5kPbj61Fzk7vAUgHKoifh_RjnXlX8OXt83A=',
         back_image = 'https://images.unsplash.com/photo-1614563393818-f595b4361b0e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fHNlYXR0bGV8ZW58MHwxfDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
         caption = choice(random_strings),
         location = choice(random_locations)),
    Post(author = users[2],
         front_image = 'https://media.istockphoto.com/id/513378132/photo/portrait-of-a-young-japanese-man-with-big-smile.jpg?s=612x612&w=0&k=20&c=r2k0Gz0zulproI5n-_ZKuKdG8cjR_tEpxGKt01LyPvM=',
         back_image = 'https://plus.unsplash.com/premium_photo-1664303623457-29f7c5779991?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTN8fHNlYXR0bGV8ZW58MHwxfDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
         caption = choice(random_strings),
         location = choice(random_locations)),
    Post(author = users[3],
         front_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwiBzJCX-OjFdVIUyCKgWtsjI0a_9g7FA2I7OU9o06cw&usqp=CAU&ec=48600113',
         back_image = 'https://images.unsplash.com/photo-1608341944160-9b947500243e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fHNlYXR0bGV8ZW58MHwxfDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
         caption = choice(random_strings),
         location = choice(random_locations)),
    Post(author = users[4],
         front_image = 'https://previews.123rf.com/images/airdone/airdone1801/airdone180100075/93806129-headshot-portrait-of-funny-attractive-young-asian-man-smiling-to-camera.jpg',
         back_image = 'https://images.unsplash.com/photo-1608341944118-f18066398b95?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fHNlYXR0bGV8ZW58MHwxfDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
         caption = choice(random_strings),
         location = choice(random_locations)),
    Post(author = users[5],
         front_image = 'https://thumbs.dreamstime.com/b/funny-silly-asian-man-trying-to-kiss-portrait-against-grey-background-160934043.jpg',
         back_image = 'https://images.unsplash.com/photo-1563663170081-4ff6736ab249?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjF8fHNlYXR0bGV8ZW58MHwxfDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
         caption = choice(random_strings),
         location = choice(random_locations)),
    Post(author = users[6],
         front_image = 'https://i.pinimg.com/474x/37/b1/ab/37b1ab7ec5fffd5b06884653c9234bd6.jpg',
         back_image = 'https://images.unsplash.com/photo-1565643119127-ba322e69e707?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjh8fHNlYXR0bGV8ZW58MHwxfDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
         caption = choice(random_strings),
         location = choice(random_locations)),
]

# randomly add friends
for index, user in enumerate(users):
    for i in range(randint(0, 6)):
        # skip self
        if i == index: 
            continue           
        user.add_friends(users[randint(0, len(users)-1)])

# add comment section and reactions to posts
for index, post in enumerate(posts):
    section = post.comments()
    for _ in range(randint(0, 10)):
        section.add_comment(random_strings[randint(0, len(random_strings)-1)])
    for user_index in range(randint(0, len(users)-1)):
        section.add_reaction(users[user_index].details['profile_icon'])

# need to separate out posts and comments in actual product
posts_path = os.path.join(os.getcwd(), 'tests/test_data/dummy_posts_data.json')
users_path = os.path.join(os.getcwd(), 'tests/test_data/dummy_users_data.json')

with open(posts_path, 'w', encoding='utf-8') as f:
    f.write('[\n')
    for i, post in enumerate(posts):
        if i == len(posts) - 1:
            f.write(f'{post.json_serialize()}\n')
            continue
        f.write(f'{post.json_serialize()},\n')
    f.write(']')
    
with open(users_path, 'w', encoding='utf-8') as f:
    f.write('[\n')
    for i, user in enumerate(users):
        if i == len(users) - 1:
            f.write(f'{user.json_serialize()}\n')
            continue
        f.write(f'{user.json_serialize()},\n')
    f.write(']')
