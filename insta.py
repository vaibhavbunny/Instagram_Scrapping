import instaloader
import os

def scrape_influencer_images(username):
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        
        if profile.is_private:
            print(f"Account '{username}' is private. Skipping...")
            return None
        elif profile.followers < 30000:
            print(f"Account '{username}' does not have more than 30k followers. Skipping...")
            return None

        print(f"Account '{username}' has {profile.followers} followers.")
        print(f"Scraping images from '{username}'...")

        folder_path = f"{username}_images"
        os.makedirs(folder_path, exist_ok=True)

        count = 0
        for post in profile.get_posts():
            if count >= 50:
                break

            if not post.is_video and post.typename == 'GraphImage':
                image_path = f"{folder_path}/{post.date_utc.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                if not os.path.exists(image_path):
                    L.download_post(post, target=image_path)
                    print(f"Scraped image: {post.url}")
                    count += 1

        print(f"Images from '{username}' have been scraped successfully.")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Account '{username}' does not exist.")
    except Exception as e:
        print(f"Error occurred while scraping images of '{username}': {e}")


if __name__ == "__main__":
    influencer_usernames = [
        "alexachung","juliaberolzheimer","imjennim","emmahill","itsnicolewallence","nicoleconcessao","nicola",
        "nicole","nicolefaria9","majawyh","garancedore","garancemarillier","inesdecominges","inesdelafressangeofficial",
        "madelynnhudson","georginagio","giorgia.andriani22","giorgiameloni","aimeelouwood","aimeebaruahofficial",
        "aimeegarcia4realz","daniellebernstein","weworewhat","mayachanout","birgitotteinterior","kensnation",
        "pilotluana","faryncorey","mariannefonseca","jennalyonsnyc","dananozime","rachellvallori","styledbya",
        "sophiehawleyweld","valeriaaherrero","imgiuliacocola","lilyrose_depp","jessieandrews","barzomer","izabelottoni",
        "mylifeaseva","vlfuller","livia_auer","jessideoliveira","amandabatula","yhasminatiphaine","lucky.sekhon",
        "sofia.artif"
    ]
    for username in influencer_usernames:
        scrape_influencer_images(username)