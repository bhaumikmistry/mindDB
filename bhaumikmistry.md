# Bhaumik Mistry

{% tabs %}
{% tab title="Profile" %}
![Profile](https://raw.githubusercontent.com/bhaumikmistry/bhaumikmistry.github.io/master/img/profile.JPG)
{% endtab %}
{% tab title="Avatar" %}
![Avatar](https://ae01.alicdn.com/kf/HTB1VrFJaI_vK1RkSmRyq6xwupXaq/6x6ft-Ninjago-Face-Eye-Red-Wall-Custom-Photo-Studio-Seamless-Background-Backdrop-Vinyl-180cm-x-180cm.jpg)
{% endtab %}
{% tab title="Casual" %}
![Casual](https://avatars3.githubusercontent.com/u/17535720?s=460&u=8653dad2c6e23f26389a0f0ddba71b30c5617a40&v=4)
{% endtab %}
{% endtabs %}

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
var data = new google.visualization.arrayToDataTable([
  ['date','z','test'],
  ['Q1-2001',1.69,1.66847553787712],
  ['Q2-2001',1.69,1.61360500808427],
  ['Q3-2001',1.42,1.49374423981914],
  ['Q4-2001',1.4,1.35653146853147],
]);
var options = {
   title: 't',
   curveType: 'none',
   width: 1500,
   height: 800,
   vAxis: {title: 'y'},
   hAxis: {title: 'x'},
   seriesType: 'scatter',
   series: {
    1: {
      type: 'line'
    }
}
};
var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
chart.draw(data, options);
}
</script>
<div id="chart_div"></div>