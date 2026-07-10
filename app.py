import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Photo Editor", layout="wide")

st.title("📷 Photo Editor using OpenCV and Streamlit")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")
    image = np.array(image)

    edited = image.copy()

    st.sidebar.header("Image Controls")

    # Resize
    width = st.sidebar.slider(
        "Width",
        100,
        1500,
        edited.shape[1]
    )

    height = st.sidebar.slider(
        "Height",
        100,
        1500,
        edited.shape[0]
    )

    edited = cv2.resize(edited, (width, height))

    # Brightness
    brightness = st.sidebar.slider(
        "Brightness",
        -100,
        100,
        0
    )

    edited = cv2.convertScaleAbs(
        edited,
        alpha=1,
        beta=brightness
    )

    # Contrast
    contrast = st.sidebar.slider(
        "Contrast",
        0.5,
        3.0,
        1.0
    )

    edited = cv2.convertScaleAbs(
        edited,
        alpha=contrast,
        beta=0
    )

    # Grayscale
    if st.sidebar.checkbox("Grayscale"):

        gray = cv2.cvtColor(
            edited,
            cv2.COLOR_RGB2GRAY
        )

        edited = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2RGB
        )

    # Blur
    blur = st.sidebar.slider(
        "Blur Strength",
        0,
        25,
        0
    )

    if blur > 0:

        k = blur if blur % 2 == 1 else blur + 1

        edited = cv2.GaussianBlur(
            edited,
            (k, k),
            0
        )

    # Warm Filter
    if st.sidebar.checkbox("Warm Filter"):

        warm = edited.copy().astype(np.float32)

        warm[:, :, 0] *= 0.9
        warm[:, :, 2] *= 1.2

        warm = np.clip(
            warm,
            0,
            255
        )

        edited = warm.astype(np.uint8)

    # Sharpen
    if st.sidebar.checkbox("Sharpen"):

        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])

        edited = cv2.filter2D(
            edited,
            -1,
            kernel
        )

    # Portrait Background Blur
    if st.sidebar.checkbox("Portrait Blur"):

        blurred = cv2.GaussianBlur(
            edited,
            (31, 31),
            0
        )

        h, w = edited.shape[:2]

        mask = np.zeros(
            (h, w),
            dtype=np.uint8
        )

        cv2.circle(
            mask,
            (w // 2, h // 2),
            min(h, w) // 3,
            255,
            -1
        )

        mask = cv2.GaussianBlur(
            mask,
            (51, 51),
            0
        )

        mask = mask / 255.0
        mask = np.dstack([mask] * 3)

        edited = (
            edited * mask +
            blurred * (1 - mask)
        ).astype(np.uint8)

    st.sidebar.markdown("---")
    st.sidebar.subheader("Extra Features")

    # Edge Detection
    if st.sidebar.checkbox("Edge Detection"):

        gray = cv2.cvtColor(
            edited,
            cv2.COLOR_RGB2GRAY
        )

        edges = cv2.Canny(
            gray,
            100,
            200
        )

        edited = cv2.cvtColor(
            edges,
            cv2.COLOR_GRAY2RGB
        )

    # Sketch Effect
    if st.sidebar.checkbox("Sketch Effect"):

        gray = cv2.cvtColor(
            edited,
            cv2.COLOR_RGB2GRAY
        )

        inverted = 255 - gray

        blur_img = cv2.GaussianBlur(
            inverted,
            (21, 21),
            0
        )

        sketch = cv2.divide(
            gray,
            255 - blur_img,
            scale=256
        )

        edited = cv2.cvtColor(
            sketch,
            cv2.COLOR_GRAY2RGB
        )

    # Cartoon Effect
    if st.sidebar.checkbox("Cartoon Effect"):

        gray = cv2.cvtColor(
            edited,
            cv2.COLOR_RGB2GRAY
        )

        gray = cv2.medianBlur(
            gray,
            5
        )

        edges = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,
            9,
            9
        )

        color = cv2.bilateralFilter(
            edited,
            9,
            250,
            250
        )

        cartoon = cv2.bitwise_and(
            color,
            color,
            mask=edges
        )

        edited = cartoon

    # Rotation
    rotation = st.sidebar.slider(
        "Rotate Image",
        0,
        360,
        0
    )

    if rotation > 0:

        h, w = edited.shape[:2]

        matrix = cv2.getRotationMatrix2D(
            (w / 2, h / 2),
            rotation,
            1
        )

        edited = cv2.warpAffine(
            edited,
            matrix,
            (w, h)
        )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(
            image,
            use_container_width=True
        )

    with col2:
        st.subheader("Edited Image")
        st.image(
            edited,
            use_container_width=True
        )

    success, buffer = cv2.imencode(
        ".png",
        cv2.cvtColor(
            edited,
            cv2.COLOR_RGB2BGR
        )
    )

    if success:

        st.download_button(
            label="📥 Download Edited Image",
            data=buffer.tobytes(),
            file_name="edited_image.png",
            mime="image/png"
        )

else:
    st.info("Upload an image to start editing.")