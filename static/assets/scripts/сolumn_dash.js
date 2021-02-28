$(function() {
     $('#push').click(function(){
        const startElement = $('#start_input');
        const endElement = $('#end_input')
        data = `api?start_date=${startElement.val()}&end_date=${endElement.val()}`


        $.ajax({
            method: 'GET',
            url: data,
            success: function(data){
              Highcharts.chart('container_2', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: `Сумма покупок за выбранный период:`
                },
                subtitle: {
                    text: `${data.total_cost} руб.`
                },
                xAxis: {
                    type: 'category',
                    labels: {
                        rotation: -45,
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Стоимость (руб)'
                    }
                },
                legend: {
                    enabled: false
                },
                tooltip: {
                    pointFormat: '<b>{point.y:.1f} руб</b>'
                },
                series: [{
                    name: 'Population',
                    data:data.series,
                    dataLabels: {
                        enabled: true,
                        rotation: -90,
                        color: '#FFFFFF',
                        align: 'right',
                        format: '{point.y}', // one decimal
                        y: 10, // 10 pixels down from the top
                        style: {
                            fontSize: '13px',
                            fontFamily: 'Verdana, sans-serif'
                        }
                    }
                }]
              });
            }
        })
     })
});
