<template>
  <div :class="className" :style="{height:height,width:width}" class="rcorners" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from '../mixins/resize'

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '600px'
    },
    autoResize: {
      type: Boolean,
      default: true
    },
    chartData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      chart: null
    }
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        console.log('Barchart -> ', val)
        this.setOptions(val)
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      this.setOptions(this.chartData)
    },
    setOptions({ title, leyenda, datos } = {}) {
      this.chart.setOption({
        grid: {
          top: '5%',
          left: '5%',
          right: '6%',
          bottom: '5%',
          containLabel: true
        },
        yAxis: [{
          // name: 'Agentes',
          type: 'category',
          data: leyenda,
          axisTick: {
            alignWithLabel: true
          },
          axisLine: {
            lineStyle: {
              color: '#303133'
            }
          },
          axisLabel: {
            interval: 0,
            show: true
          }
        }],
        xAxis: [{
          name: 'Procesos',
          type: 'value',
          axisTick: {
            show: false
          },
          axisLine: {
            lineStyle: {
              color: '#303133'
            }
          }
        }],
        series: [{
          type: 'bar',
          barWidth: '70%',
          data: datos,
          animationDuration: 5000
        }],
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          },
          formatter: function(obj) {
            return '<div style="border-bottom: 1px solid rgba(255,255,255,.3); font-size: 14px;padding-bottom: 7px;margin-bottom: 7px">' +
                            '<strong>' + obj[0].name + '</strong>' +
                            '</div> <strong>Cantidad procesos: </strong>' + obj[0].value
          }
        }
        // color: ['#344b58', '#4cabce', '#e5323e']
      })
    }
  }
}
</script>
