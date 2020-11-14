from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='alexander')
        u.set_password('supersecret')
        self.assertFalse(u.check_password('notsecret'))
        self.assertTrue(u.check_password('supersecret'))

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

    def test_follow(self):
        alexander = User(username='alexander', email='alexander@email.com')
        luna = User(username='luna', email='luna@email.com')
        db.session.add(alexander)
        db.session.add(luna)
        db.session.commit()
        self.assertEqual(alexander.followed.all(), [])
        self.assertEqual(alexander.followers.all(), [])

        alexander.follow(luna)
        db.session.commit()
        self.assertTrue(alexander.is_following(luna))
        self.assertEqual(alexander.followed.count(), 1)
        self.assertEqual(alexander.followed.first().username, 'luna')
        self.assertEqual(luna.followers.count(), 1)
        self.assertEqual(luna.followers.first().username, 'alexander')

        alexander.unfollow(luna)
        db.session.commit()
        self.assertFalse(alexander.is_following(luna))
        self.assertEqual(alexander.followed.count(), 0)
        self.assertEqual(luna.followers.count(), 0)

    def test_follow_posts(self):
        alexander = User(username='alexander', email='alexander@email.com')
        luna = User(username='luna', email='luna@email.com')
        conan = User(username='conan', email='conan@email.com')
        doyle = User(username='doyle', email='doyle@email.com')
        db.session.add_all([alexander, luna, conan, doyle])

        now = datetime.utcnow()
        post_alexander = Post(
            body="post from alexander",
            author=alexander,
            timestamp=now + timedelta(seconds=1)
        )
        post_luna = Post(
            body="post from luna",
            author=luna,
            timestamp=now + timedelta(seconds=4)
        )
        post_conan = Post(
            body="post from conan",
            author=conan,
            timestamp=now + timedelta(seconds=3)
        )
        post_doyle = Post(
            body="post from doyle",
            author=doyle,
            timestamp=now + timedelta(seconds=2)
        )
        db.session.add_all([post_alexander, post_luna, post_conan, post_doyle])
        db.session.commit()

        alexander.follow(luna)
        alexander.follow(doyle)
        luna.follow(conan)
        conan.follow(doyle)
        db.session.commit()

        f1 = alexander.followed_posts().all()
        f2 = luna.followed_posts().all()
        f3 = conan.followed_posts().all()
        f4 = doyle.followed_posts().all()
        self.assertEqual(f1, [post_luna, post_doyle, post_alexander])
        self.assertEqual(f2, [post_luna, post_conan])
        self.assertEqual(f3, [post_conan, post_doyle])
        self.assertEqual(f4, [post_doyle])


if __name__ == '__main__':
    unittest.main(verbosity=2)
