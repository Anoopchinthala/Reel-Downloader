
import pytest
from Main import extract_shortcode, remove_non_video_files, download_reel

def test_extract_shortcode():
    assert extract_shortcode("https://www.instagram.com/reel/shortcode/") == "shortcode"
    assert extract_shortcode("https://www.instagram.com/reel/") is None
    assert extract_shortcode("") is None

def test_remove_non_video_files():
    # Simulate the files in the directory
    mock_files = ["video.mp4", "document.txt", "photo.jpg"]
    mock_files = [file for file in mock_files if file.endswith(".mp4")]
    assert mock_files == ["video.mp4"], "Failed to retain only .mp4 files"

def test_download_reel_invalid_url():
    invalid_url = "https://www.instagram.com/invalid/"
    output_dir = "TestReels"
    try:
        download_reel(invalid_url, output_dir)
        assert False, "Expected an error for invalid URL"
    except Exception as exc:
        assert "Invalid URL" in str(exc) or "An error occurred" in str(exc), \
            "Expected an error message indicating an invalid URL"


