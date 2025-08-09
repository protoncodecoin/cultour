const BASEURL = location.host;
let guestsElement = document.querySelector(".guests__field");
let notes = document.querySelector(".note__field");
let paymentBtn = document.querySelector('.initiate__btn');
let bookTourBtn = document.querySelector(".book__tour");

let {tourist, email} = userInfo;

console.log(tourist, email);

let csrftoken = getCookie("csrftoken");
let tourId = null;
let tourAmount = null;

bookTourBtn.addEventListener("click", function(e){
    const target = e.target;
    console.log(target)

    if (target.classList.contains("tour__cls")) {
        tourId = target.dataset.tourId;
        tourAmount = target.dataset.tourFee;

    }
})


paymentBtn.addEventListener("click", async function(e) {

    // console.log(tourId, tourAmount, guestsElement.value, amount);
    
    document.querySelector(".first-close-btn").click();

    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            tourist,
            tour: Number(tourId),
            guests: guestsElement.value,
            notes: notes.value,
            amount: tourAmount,
        }),
    };

    const URL = `/api/tours/reservations/`;

    try {
        const response = await fetch(URL, options);

        if (!response.ok) {
            throw new Error("Failed to reserve hotel")
        }

        const jsonData = await response.json();

        console.log(jsonData);

        payWithPaystack(jsonData["ref"], jsonData["amount"], jsonData["object_id"], jsonData["content_type"])

        // return jsonData

    } catch (error) {
        console.log(error);
    }


});



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



function payWithPaystack(ref, amount, tourId, content_type) {
    let currency = "GHS";
    let plan = "";

    let obj = {
        key: "pk_test_17f45c77fbf0880f64302e5ac67425741af647fa",
        amount,
        ref,
        email,
        callback: function(response) {
            // call verify function
            verifyPayment(ref, content_type, tourId)
        },
    };

    if (Boolean(currency)) {
        obj.currency = currency;
    }

    if (Boolean(plan)) {
        obj.plan - plan;
    }

    var handler = PaystackPop.setup(obj);
    handler.openIframe();
    
}


async function verifyPayment(ref, content_type, obj_id) {

    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            ref,
            content_type,
            object_id: obj_id,
        }),
    };

    const URL = `/api/payment/verify/`;

    try {
        
        const response = await fetch(URL, options);

        if (!response.ok) {
            console.log(response.statusText);
            throw new Error("Failed to verify transaction")
        }

        const jsonData = await response.json();

        return jsonData;
    } catch (error) {
        console.log(error)
    }

}