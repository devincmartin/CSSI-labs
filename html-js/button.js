let button = document.querySelector("#like-button");
let like_header = document.querySelector("#my-likes")
let like_count = 0
button.addEventListener("click", () => {
    // console.log("I liked it!");
  like_count++;
  like_header.innerHTML = "You have " + like_count + " likes."
});

const changeHeaderColor= () => {
  like_header.style.color = "tomato";
}

like_header.addEventListener("click", changeHeaderColor)
