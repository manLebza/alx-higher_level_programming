const $ = window.$;
$.get('https://swapi.co/api/people/5/?format=json',function (data, textStatus) {
  $('DIV#charactor').text(data.name);
});
