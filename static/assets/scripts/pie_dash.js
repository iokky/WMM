$(function () {
     $('#push').click(function(){
        const startElement = $('#start_input');
        const endElement = $('#end_input')
        data = `api?start_date=${startElement.val()}&end_date=${endElement.val()}`

        $.ajax({
            method: 'GET',
            url: data,
            success: function(data){
              Highcharts.chart('container', {
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false,
                    type: 'pie'
                },
                title: {
                    text: 'Доля расходов по продуктам'
                },
                tooltip: {
                    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                },
                accessibility: {
                    point: {
                        valueSuffix: '%'
                    }
                },
                plotOptions: {
                    pie: {
                        allowPointSelect: true,
                        cursor: 'pointer',
                        dataLabels: {
                            enabled: true,
                            format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                            connectorColor: 'silver'
                        }
                    }
                },
                series: [{
                    name: 'Продукт',
                    data: data.series
                }]
              });
            }
        })
     })
});