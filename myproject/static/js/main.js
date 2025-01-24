jQuery(document).ready(function() {
  jQuery('body').on('click', '#sidebarCollapse', function() {
    jQuery('#sidebar').toggleClass('active');
  });
});

jQuery(document).ready(function() {
  jQuery('body').on('click', '#sidebarCollapseClose', function() {
    jQuery('#sidebar').toggleClass('active');
  });
});

// This code activates flatpickr on fields with the 'datetimefield' class when the document has loaded
window.addEventListener("DOMContentLoaded", function () {
    flatpickr(".datetimefield", {
        enableTime: true,
        enableSeconds: true,
        dateFormat: "Y-m-d H:i:S",
    });
});



$(document).ready(function() {
  // Итерируемся по всем напоминаниям на странице
  $(".reminder").each(function() {
    // Получаем время напоминания и переводим его в миллисекунды
var dateString = $(this).find(".date").text();
var dateParts = dateString.split(/[.: ]/);
var time = new Date(dateParts[2], dateParts[1]-1, dateParts[0], dateParts[3], dateParts[4]).getTime();

    // Получаем текущее время и переводим его в миллисекунды
    var currentTime = new Date().getTime();


    // Если время напоминания меньше или равно текущему времени,
    // то воспроизводим звуковой сигнал
    if (time <= (currentTime+10000) && time>=(currentTime-2000)) {
      var audio = $("#notification-sound")[0];
      audio.volume = 0.05;
      audio.play();
    }
    // Если время напоминания больше текущего времени,
    // то задаем задержку перед вызовом функции воспроизведения звукового сигнала

  });

});
