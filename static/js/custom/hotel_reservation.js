const BASEURL = location.host;
let saveBtn = document.querySelector(".save__btn");
let checkInEl = document.querySelector(".check")
console.log("worked");

const { roomId, hotelId } = window.bookingInfo;
console.log(roomId, hotelId)


let csrftoken = getCookie("csrftoken");

saveBtn.addEventListener("click", async function(e){
   
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

async function createTableReservation(tableId) {

    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
                    "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            hotel_id: hotelId,
            room_id: roomId,
            check_in_date: checkInEl.value,
            check_out_date: checkOutEl.value,
            guests: guestsElement.value,
            notes: notes
        }),
    }

    const URL = `http://${BASEURL}/api/create-reservation/`;


    try {
        const response = await fetch(URL, options);

        if (!response.ok) {
            throw new Error("Failed to book reservation");
        }

        const respData = await response.json();
        console.log(respData);

        // ✅ Close the modal the Bootstrap 5 way
        document.querySelector(".first-close-btn").click();

        // TODO: Fix response modal not showing
        // show second modal
        // secondModal.click();
        document.getElementById("hiddenBookButton").click();


    } catch (error) {

        document.querySelector(".first-close-btn").click();

        document.getElementById("hiddenBookButton").click();
    }
}

