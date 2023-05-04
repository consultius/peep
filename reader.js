console.log("reader.js script is running");

document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM content loaded");

  document.getElementById("read-text").addEventListener("click", function () {
    console.log("Read Text button clicked");
    const text = document.getElementById("text-container").innerText;
    const utterance = new SpeechSynthesisUtterance(text);

    // You can customize the voice, pitch, and rate here
    // utterance.voice = window.speechSynthesis.getVoices()[1]; // Choose a voice
    // utterance.pitch = 1; // 0 to 2, default is 1
    // utterance.rate = 1; // 0.1 to 10, default is 1

    window.speechSynthesis.speak(utterance);
  });
});
