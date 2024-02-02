import instaloader

instagram = instaloader.Instaloader()
username = input("Enter your username: ")

profile = instaloader.Profile.from_username(instagram.context, username)

private = profile.is_private

if not private:
    posts = list(profile.get_posts())
    latest_post = posts[0]
    instagram.download_post(latest_post, target = profile.username)
    