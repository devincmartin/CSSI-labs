// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


//
// window.addEventListener("keypress", (e) => {
//   console.log(e.keyCode);
// });

// let button = document.querySelector("#box1");
// let like_header = document.querySelector("#my-likes")
// let like_count = 0
// button.addEventListener("click", () => {
//     // console.log("I liked it!");
//   like_count++;
//   like_header.innerHTML = "You have " + like_count + " likes."
// });

console.log("Running Click Events Script");

const box1= document.querySelector("#box1");
const box2= document.querySelector("#box2");
const box3= document.querySelector("#box3");

const changeBoxColors = (color) => {
  box1.style.backgroundColor = color;
  box2.style.backgroundColor = color;
  box3.style.backgroundColor = color;
}

// const changeBoxColorsPink = () => {
//   box1.style.backgroundColor = "pink"
//   box3.style.backgroundColor = "pink"
//}

box1.addEventListener("click", () => {
  changeBoxColors("red");
});

box2.addEventListener("click", () => {
  changeBoxColors("pink");
});

box3.addEventListener("click", () => {
  changeBoxColors("orange");
})

const box4 = document.querySelector("#box4");
const box5 = document.querySelector("#box5");

box4.addEventListener("click", () => {
  box4.classList.toggle("active");
  box5.classList.toggle("active");
})


// Get the button, and when the user clicks on it, execute myFunction
// box4.document.getElementById("click").onclick = changeBoxColors() {myFunction()};

/* myFunction toggles between adding and removing the show class, which is used to hide and show the dropdown content */
// function myFunction() {
//   document.getElementById("myDropdown").classList.toggle("show");
// }









// box2.addEventListener("click", changeBoxColorsPink);

// let box4= document.querySelector("#box4")
// let box5= document.querySelector("#box5")
