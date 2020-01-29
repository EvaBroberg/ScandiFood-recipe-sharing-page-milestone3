//Slideshow

;(function() {

    var slider = function() {
      
      var backImg = [];
      backImg[0] = "static/img/slide1.jpg";
      backImg[1] = "static/img/slide2.jpg";
      backImg[2] = "static/img/slide3.jpg";
      
      var i = 0;
      var x = (backImg.length) - 1;
      var int = 3500;
      
      interval = setInterval(showNext, int); // hoist?
      
      var elements = {
        slider: document.querySelector('.slider'),
        btn: { 
          left: document.querySelector('.btnLeft'),
          right: document.querySelector('.btnRight')
        }
      }
      
      var startInterval = function() {
         interval = setInterval(showNext, int);
      }
      
      var stopInterval = function() {
        clearInterval(interval);
      }
      
      var attachEvents = function() {
        elements.btn.left.onclick = function() { showPrevious(); };
        elements.btn.right.onclick = function() {  showNext(); };
        elements.slider.addEventListener("mouseenter", stopInterval);
        elements.slider.addEventListener("mouseleave", startInterval);
      };
      
      var changeImg = function() {
        elements.slider.style.backgroundImage = 'url(' + backImg[i] + ')';
      }
      
      var initialize = (function() {
        attachEvents();
        changeImg(i);
      })();
  
      var showPrevious = function() {
        (i <= 0) ? i = 3 : i--;
        changeImg(i);
      };
  
      var showNext = function() {
        (i >= x) ? i = 0 : i++;
        changeImg(i);
      };
  
    };
  
    slider();
  
  })();
  
  // Hide elements that are not selected
  function w3RemoveClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
      while (arr1.indexOf(arr2[i]) > -1) {
        arr1.splice(arr1.indexOf(arr2[i]), 1);
      }
    }
    element.className = arr1.join(" ");
  }
  
  // Add active class to the current control button (highlight it)
  var btnContainer = document.getElementById("myBtnContainer");
  var btns = btnContainer.getElementsByClassName("btn");
  for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
      var current = document.getElementsByClassName("active");
      current[0].className = current[0].className.replace(" active", "");
      this.className += "active";
    });
  }