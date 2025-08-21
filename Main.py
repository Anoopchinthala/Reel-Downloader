
import os
import instaloader

def main():
    reel_url = input("Enter the reel's URL: ").strip()
    output_folder = "Reels"
    download_reel(reel_url, output_folder)

def download_reel(reel_url, output="Reels"):
    try:
        reels = instaloader.Instaloader()
        reels.download_videos = True        # only videos are downloaded
        reels.download_comments = False     # Skips comments
        reels.save_metadata = False         # Skips metadata files (e.g., JSON)
        reels.download_geotags = False      # Skips geotags
        reels.save_captions = False         # Skips captions
        short = extract_shortcode(reel_url) # Extracts shortcode from URL
        if not short:
            raise ValueError("Invalid URL.")  # Raise an exception for invalid URL
        if not os.path.exists(output):        # Sets output directory
            os.makedirs(output)
        reels.dirname_pattern = output
        print(f"Downloading...")             
        post = instaloader.Post.from_shortcode(reels.context, short)
        reels.download_post(post, target=output)
        remove_non_video_files(output)        # Removes unwanted files, leaving only the video.
        print(f"Download finished. Check the '{output}' folder.")
    except instaloader.exceptions.InstaloaderException as e:
        raise Exception(f"An error occurred: {e}")  # Raise exception on instaloader error
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")  # Raise exception for unexpected errors

def extract_shortcode(reel_url):
    try:
        parts = reel_url.split("/")
        if len(parts) < 5 or not parts[-2] or parts[-2] == "reel":
            return None                        # Return None for invalid URL
        return parts[-2]
    except IndexError:
        return None

def remove_non_video_files(directory):
    for file in os.listdir(directory):
        if not file.endswith(".mp4"):
            os.remove(os.path.join(directory, file))

if __name__ == "__main__":
    main()


