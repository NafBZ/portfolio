from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

total_posts = [
    {
        "slug":"abtest",
        "image":"av.png",
        "author":"Hinton",
        "date": date(2023, 9, 29),
        "title": "A/B Testing",
        "excerpt": """
                    Field Robotic Systems at the University de Girona, Spain, and the University of Zagreb, Croatia.""",
        "content": """A statistical way of comparing two (or more) techniques—the A and the B.
                    Typically, the A is an existing technique, and the B is a new technique.
                    A/B testing not only determines which technique performs better but also
                    whether the difference is statistically significant. A/B testing usually
                    compares a single metric on two techniques; for example, how does model
                    accuracy compare for two techniques? However, A/B testing can also compare
                    any finite number of metrics."""
    },
    {
        "slug":"abtestV2",
        "image":"av.png",
        "author":"Hinton",
        "date": date(2023, 10, 29),
        "title": "2nd A/B Testing",
        "excerpt": """Lalallalal Calo lage na""",
        "content": """A statistical way of comparing two (or more) techniques—the A and the B.
                    Typically, the A is an existing technique, and the B is a new technique.
                    A/B testing not only determines which technique performs better but also
                    whether the difference is statistically significant. A/B testing usually
                    compares a single metric on two techniques; for example, how does model
                    accuracy compare for two techniques? However, A/B testing can also compare
                    any finite number of metrics."""
    }
]

def get_date(post):
    return post['date']


def landing_page(request):
    sorted_posts = sorted(total_posts, key=get_date)
    last_post = sorted_posts[:]
    return render(request, "blog/index.html", {
        "posts": last_post
    })

def all_posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": total_posts
    }
    )

def post_detail(request, slug):
    identified_post = next(post for post in total_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    }
    )