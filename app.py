import streamlit as st
import time

# Sample test videos (Replace with actual paths)
SAMPLE_VIDEOS = {
    "Test sample 1": "videos/fire.mp4",
    "Test sample 2": "videos/burglary.mp4",
    "Test sample 3": "videos/vandalism1.mp4",
}

# Incident categories (matching test samples)
CATEGORIES = {
    "Test sample 1": "Fire Incident",
    "Test sample 2": "Burglary Attempt",
    "Test sample 3": "Vandalism in Progress",
}

# Streamlit UI
st.title("🔍 Smart CCTV Incident Detector")
st.subheader("Hey user!\n This is a demo of our solution. The AI model isn't trained yet, but you can pick a sample video to see how it will work. Feel free to play around.")

# User selects a sample video
selected_sample = st.selectbox("🎥 Select a sample video", ["None"] + list(SAMPLE_VIDEOS.keys()))

# Display video if a sample is chosen
if selected_sample != "None":
    st.video(SAMPLE_VIDEOS[selected_sample])

    # Analyze Video
    if st.button("🚀 Analyze Video"):
        st.write("⏳ Running classification... (this will take a few seconds)")
        time.sleep(3)
        # Print output in required format
        detected_activity = CATEGORIES[selected_sample]
        print(f"Our Deep Network Model has detected: {detected_activity}")

        # Display result
        st.success(f"✅ **Detected Activity:** {detected_activity}")
        st.info("⚠️ Review recommended!")
