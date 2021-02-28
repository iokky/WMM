// SideBar
$(function () {

  let open = $('#open');
  let menu = $('#side_bar_menu');

  $('#side_bar_headding').click(function () {
    open.css('visibility', 'visible')
    menu.animate({
      left: '-=1000',
      }, 660, function () {})
  }),

  $('#open').click(function () {
    open.css('visibility', 'hidden')
    menu.animate({
      left: '0',
    },680, function () {})
  })

})


// Table
$(function () {
    $('#push').click(function(){
        const startElement = $('#start_input');
        const endElement = $('#end_input')
        data = `api?start_date=${startElement.val()}&end_date=${endElement.val()}`

         $.ajax({
            method: 'GET',
            url: data,
            success: function(data){
                $('#table_body').empty();
                $('#cat_filter').empty();

                $.each(data.series, function(key, object){
                    const wrapper = $('<tr/>')
                    const average = Math.round(object.y / object.count)

                    $('#cat_filter').append(
                       $('<button/>', { text: object.name }).addClass('btn-primary btn-block cat_btn')
                    )
                    $(wrapper).append(
                        $('<th/>', { text: object.name}),
                        $('<th/>', { text: `${object.y} руб`}),
                        $('<th/>', { text: `${object.count} ед`}),
                        $('<th/>', { text: `${average} руб`}),
                    ),
                    $('#table_body').append(wrapper);
                })
            }
         })
    })
}),

$(document).on('click', '.cat_btn', function(eventObject){
    event.stopPropagation();
    event.stopImmediatePropagation();
    let elem = $(this).text()
    series = []
    totalCost = 0

    $.ajax({
        method: 'GET',
        url: data,
        success: function(data){
            $.each(data.products, function(){
               if (this.category == elem){
                  totalCost += this.y
                  series.push(this)


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
                        data: series
                    }]
                  });
                  Highcharts.chart('container_2', {
                    chart: {
                        type: 'column'
                    },
                    title: {
                        text: `Сумма покупок за выбранный период:`
                    },
                    subtitle: {
                        text: `${totalCost} руб.`
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
                        data: series,
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
        }
    })
})

