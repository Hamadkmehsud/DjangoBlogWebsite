from django.shortcuts import render
from datetime import date 
# Create your views here.

posts_blog = [
    {
        'slug' : 'practic-coding-daily',
        'image' : 'landscap2.jpg',
        'author' : 'Hammad Khan',
        'date' : date(2022, 3, 8),
        'title' : 'How to become a Pro',
        'excerpt' : 'The Power of Daily Coding: Why Consistency Matters for Developers',
        'content' : """ In the fast-paced world of technology, the most successful developers aren't necessarily the ones who know the most programming languages or have the flashiest resumes. Instead, they're often the ones who code every single day, practicing their craft consistently and building their skills brick by brick. Daily coding isn't just a routine—it's a mindset. Whether you’re a beginner or an experienced coder, developing a habit of coding daily can be transformative.
        Here’s why daily coding is such a game-changer and how you can make it work for you."""
    },
    {
        'slug' : 'about_hammad',
        'image' : 'me.jpg',
        'author' : 'Hammad Khan',
        'date' : date(2021, 3, 1),
        'title' : 'Who is Hammad Khan',
        'excerpt' : 'Aspring Django web Developer',
        'content' : """ Muhammad Hammad Khan is an associate web developer currently focused on learning Python and working with Django, HTML, CSS, and JavaScript, with a keen interest in networking and system administration. He enjoys playing cricket and researching various topics. Hammad is developing a blog project that features dynamic content and slugs in URLs, aiming for a professional look for his personal webpage. He is open to sharing his social media links, including Facebook and Instagram."""
    },
    {
        'slug' : 'to_become_loser',
        'image' : 'landscap.jpg',
        'author' : 'Hammad Khan',
        'date' : date(2024, 12, 19),
        'title' : 'how to become a loser!',
        'excerpt' : 'The Case for Not Coding Daily: Why Balance is Key for Developers',
        'content' : """ One of the biggest dangers of coding daily is the risk of burnout. Coding is a mentally intensive activity that requires focus, problem-solving, and creativity. When you push yourself to code every single day without adequate rest, you run the risk of burning out, losing your passion for programming, and feeling exhausted.
        Example: Imagine working on a complex project late into the night, only to wake up the next day and force yourself to code again. The result? Mental fatigue, frustration, and diminished productivity.
        Taking time off from coding, even for just a day or two, gives your brain a chance to recharge. Breaks allow you to return to coding with fresh energy and renewed creativity."""
    }
]

def get_date(dict):
    get_date = dict['date']
    return get_date

def main_page(request):
    sorted_posts = sorted(posts_blog ,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/main_page.html',{
        "b_post": latest_posts
    })

def all_posts(request):
    return render(request, 'blog/all_posts.html',{
        "all_posts" : posts_blog
    })
def post_details(request,slug):
    identified_post = next(post for post in posts_blog if post['slug'] == slug )
    return render(request, 'blog/post_detail_page.html',{
        "post": identified_post
    })