gsap.registerPlugin(ScrollTrigger);

// Scene animations
gsap.from(".scene1 .content", { y: 100, opacity: 0, duration: 1.5 });
gsap.from(".scene2 .content", {
  scrollTrigger: { trigger: ".scene2", start: "top 80%" },
  y: 100, opacity: 0, duration: 1.5
});
gsap.from(".scene3 .content", {
  scrollTrigger: { trigger: ".scene3", start: "top 80%" },
  y: 100, opacity: 0, duration: 1.5
});

// Play music after user interaction (autoplay restrictions)
document.body.addEventListener("click", () => {
  document.getElementById("bg-music").play();
});
