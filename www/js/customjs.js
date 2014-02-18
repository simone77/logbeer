 /**
 * Request data from the server, add it to the graph and set a timeout to request again
 */
$(document).ready(function() {
    Highcharts.setOptions({ global : { useUTF: true } });
    var options = {
	chart: {
	    type: 'spline',
            renderTo: 'container',
	    zoomType: 'x'
        },
            xAxis: {
                type: 'datetime',
		title:{ text: 'Tempo'},
            gridLineWidth: 1,
                labels: {
                   formatter: function() {
                      return Highcharts.dateFormat('%d-%m %H:%M:%S', this.value);
                }
        }
		
            },
	yAxis:{
		title:{ text: 'Temperatura'},
		min: 0
	},
	plotOptions: {
            series: {
                marker: {
                    enabled: false
                }
            }
        },
        series: [{}]
    };

    $.getJSON('server.py', function(data) {
        options.series[0].data = data;
        var chart = new Highcharts.Chart(options);
    });

});
