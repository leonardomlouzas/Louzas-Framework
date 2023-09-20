from louzas import Louzas
from controllers import get_posts_from_database, add_new_post

app = Louzas()


@app.route(r"^/$", template="list.template.html")
def post_list():
    posts = get_posts_from_database()
    return {"post_list": posts}


@app.route(r"^/api$")
def post_list_api():
    posts = get_posts_from_database()
    return {"post_list": posts}, "200 Ok", "application/json"


@app.route(r"^/(?P<id>\d{1,})$", template="post.template.html")
def post_detail(id):
    post = get_posts_from_database(post_id=id)[0]
    return {"post": post}


@app.route(r"^/new$", template="form.template.html")
def new_post_form():
    return {}


@app.route(r"^new$", method="POST")
def new_post_add(form):
    post = {item.name: item.value for item in form.list}
    add_new_post(post)
    return "<strong>New post created!</strong>", "201 Created", "text/plain"


if __name__ == "__main__":
    app.run()