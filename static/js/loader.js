window.onload = function () {
  load_1();
  load_2();
};

async function load_1() {
  const container_loader = document.querySelector(".container_loader");
  container_loader.style.opacity = 0;
  container_loader.style.visibility = "hidden";
}

async function load_2() {
  const container_loader = document.querySelector(".container_loader2");
    container_loader.style.opacity = 0;
    container_loader.style.visibility = "hidden";
}