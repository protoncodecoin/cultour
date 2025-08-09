let currentModel = null;
let currentObjectId = null;
let relatedModel = null;

// Handle modal trigger to store model and object ID
document.querySelectorAll('[data-toggle="modal"]').forEach(button => {
    button.addEventListener('click', () => {
        currentModel = button.getAttribute('data-model-name');
        currentObjectId = button.getAttribute('data-object-id');
        relatedModel = button.getAttribute('data-related-model');
    });
});

// Handle rating submission
document.querySelector('.submit-rating').addEventListener('click', async function () {
    const ratingInput = document.querySelector('input[name="rating"]:checked');
    const comment = document.querySelector(".rating-feedback textarea").value;

    console.log(currentModel, currentObjectId, relatedModel);

    if (!ratingInput) {
        alert("Please select a rating before submitting.");
        return;
    }

    if (!currentModel || !currentObjectId || !relatedModel) {
        alert("Model or object ID is missing.");
        return;
    }

    const payload = {
        rating: parseInt(ratingInput.value),
        comment: comment,
        model: currentModel,
        object_id: parseInt(currentObjectId),
        related_model: relatedModel,
    };

    console.log(payload)

    try {
        const response = await fetch("/api/ratings/create-rating/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.ok) {
            alert("Thanks for your rating!");

            // Reset form
            document.querySelector(".rating-feedback textarea").value = "";
            document.querySelectorAll('input[name="rating"]').forEach(input => input.checked = false);

            // Close modal manually
            const modal = document.getElementById("exampleModal");
            modal.classList.remove("show");
            modal.setAttribute("aria-hidden", "true");
            modal.style.display = "none";
            document.body.classList.remove("modal-open");

            // Remove backdrop
            const backdrop = document.querySelector(".modal-backdrop");
            if (backdrop) backdrop.remove();

        } else {
            alert("Error: " + (data.detail || JSON.stringify(data)));
        }

    } catch (error) {
        console.error("Error submitting rating:", error);
        alert("An error occurred while submitting your rating.");
    }
});

// Helper to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

