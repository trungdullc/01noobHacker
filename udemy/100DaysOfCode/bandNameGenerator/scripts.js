// Note: Uses jquery instead of vanilla JS
// jQuery (Old) vs modern JS
/*
# Selecting elements
$("#run-button")                          document.getElementById("run-button")                 document.querySelector("#run-button");
$("#Content")                             document.getElementById("Content")                    document.querySelector("#Content");
$("#" + CurrentId + " input")             document.querySelector("#" + CurrentId + " input")    document.querySelector(`#${CurrentId} input`);

# Waiting for the page to load
$(document).ready(function () {           document.addEventListener("DOMContentLoaded", function () {
  // code                                   // code
});                                       });

# Attaching event listeners
$("#run-button").click(function () { ... });      document.getElementById("run-button")
                                                    .addEventListener("click", function () { ... });
$(document).on("keydown", function (e) { ... });
                                                  document.addEventListener("keydown", function (e) { ... });
# Reading and writing values
$("#id input").val();        // get value         input.value;
line.attr("size", "1");     // set attribute      input.setAttribute("size", "1");
line.prop("disabled", true);                      input.disabled = true;

# Adding HTML to the page
$("#Content").append("<div>Text</div>");          document.getElementById("Content")
                                                    .insertAdjacentHTML("beforeend", "<div>Text</div>");

# Side Quest: JavaScript 3 common ways to pass a fx
document.getElementById("run-button")             // Inline anonymous function
  .addEventListener("click", function () {
    console.log("Clicked!");
  });

document.getElementById("run-button")           // Arrow function
  .addEventListener("click", () => {
    console.log("Clicked!");
  });

function handleRunClick() {                   // Named function, C/C++ like
  console.log("Clicked!");
}

document.getElementById("run-button")
  .addEventListener("click", handleRunClick);
*/

// Current line
var CurrentId = undefined;

var inputValues = [];
var bandName = "";
const inputPrompts = ["What's your pet's name?"];
let isFirstClick = true;
let isOn = true;

// Click Run
$(document).ready(function () {
  $("#run-button").click(function () {
    isOn = true;
    inputValues = [];
    var bandName = "";
    $("#Content").empty();
    NewLine("Welcome to the Band Name Generator.", false);
    NewLine("What's the name of the city you grew up in?", true);
  });
});

// Enter button
$(document).on("keydown", function (e) {
  var x = event.which || event.keyCode;
  if (x == 13 && isOn) {
    var consoleLine = $("#" + CurrentId + " input").val();

    console.log(consoleLine);
    bandName += ` ${consoleLine}`;
    inputValues.push({ id: CurrentId, val: consoleLine });

    console.log(inputValues);

    if (inputValues.length > inputPrompts.length) {
      console.log("called");
      NewLine("Your band name could be " + bandName, false);

      $(".console-carrot").remove();
      isOn = false;
      return;
    }

    $(".console-carrot").remove();

    NewLine(inputPrompts[inputValues.length - 1], true);
    // setTimeout(NewLine, delay);
  }
});
$(document).on("keydown", function (e) {
  var x = event.which || event.keyCode;
  var line = $("#" + CurrentId + " input");
  var length = line.val().length;
  if (x != 8) {
    line.attr("size", 1 + length);
  } else {
    line.attr("size", length * 0.95);
  }
  if (length === 0) {
    $("#" + CurrentId + " input").attr("size", "1");
  }
});
$(document).on("click", function (e) {
  $("#" + CurrentId + " input").focus();
});

// New line
function NewLine(text, isPrompt) {
  if (CurrentId !== undefined) {
    $("#" + CurrentId + " input").prop("disabled", true);
  }
  CurrentId = "consoleInput-" + GenerateId();

  if (isPrompt) {
    // New line input
    $("#Content").append("<div>" + text + "</div>");
    $("#Content").append(
      '<div id="' +
        CurrentId +
        '">' +
        '<input autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" type="text" class="terminal-input" /><div class="console-carrot"></div></div>'
    );
    $("#" + CurrentId + " input").focus();
    $("#" + CurrentId + " input").attr("size", "1");
  } else {
    $("#Content").append('<div id="' + CurrentId + '">' + text + "</div>");
  }
}

function GenerateId() {
  return Math.random().toString(16).slice(2);
}