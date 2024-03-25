const tgCheckBox = document.getElementById("tg");
const tgDescript = document.getElementById("tg-description");
const vkCheckBox = document.getElementById("vk");
const vkDescript = document.getElementById("vk-description");

tgCheckBox.addEventListener("change", () => {
  if (tgDescript.hidden === true) {
    tgDescript.hidden = false;
    console.log(1);
  } else {
    tgDescript.hidden = true;
  }
});

vkCheckBox.addEventListener("change", () => {
  if (vkDescript.hidden === true) {
    vkDescript.hidden = false;
    console.log(1);
  } else {
    vkDescript.hidden = true;
  }
});
