
///Navigation

let content = document.getElementById("container")
let content2 = document.getElementById("container2")
let content3 = document.getElementById("container3")
let content4 = document.getElementById("container4")
let content5 = document.getElementById("container5")
let content6 = document.getElementById("container6")
let full = document.getElementById("Full graph")
let week = document.getElementById("Week")
let month = document.getElementById("Month")
let year = document.getElementById("Year")
let total = document.getElementById("Total")
let popular = document.getElementById("Popular Time")

full.addEventListener("click", () => {
    content.style.display = "grid"
    content2.style.display = "none"
    content3.style.display = "none"
    content4.style.display = "none"
    content5.style.display = "none"
    content6.style.display = "none"
})

week.addEventListener("click", () => {
    content.style.display = "none"
    content2.style.display = "grid"
    content3.style.display = "none"
    content4.style.display = "none"
    content5.style.display = "none"
    content6.style.display = "none"
})


month.addEventListener("click", () => {
    content.style.display = "none"
    content2.style.display = "none"
    content3.style.display = "grid"
    content4.style.display = "none"
    content5.style.display = "none"
    content6.style.display = "none"
})


year.addEventListener("click", () => {
    content.style.display = "none"
    content2.style.display = "none"
    content3.style.display = "none"
    content4.style.display = "grid"
    content5.style.display = "none"
    content6.style.display = "none"
})

total.addEventListener("click", () => {
    content.style.display = "none"
    content2.style.display = "none"
    content3.style.display = "none"
    content4.style.display = "none"
    content5.style.display = "grid"
    content6.style.display = "none"
})

popular.addEventListener("click", () => {
    content.style.display = "none"
    content2.style.display = "none"
    content3.style.display = "none"
    content4.style.display = "none"
    content5.style.display = "none"
    content6.style.display = "grid"
})