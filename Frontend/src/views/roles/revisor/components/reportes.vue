<template>
  <div class="components-container">
    <el-row>
      <el-col :span="24" style="border: 0px solid red; text-align: center;">
        <aside>
          <span style="color: black; font-size: 170%;">
            <b>DIRECCIÓN TÉCNICA DE GESTIÓN DE ENERGÍA</b>
          </span>
        </aside>
      </el-col>
      <el-col :span="24" style="border: 0px solid red; text-align: center;">
        <aside>
          <span style="font-size: 120%;">
            <b>{{ name }}</b>
          </span>
        </aside>
      </el-col>

      <el-card class="box-card card-header">
        <div slot="header" class="clearfix">
          <span>
            <b>REPORTES</b>
          </span>
        </div>
      </el-card>

      <el-col :span="24" style="border: 0px solid red; text-align: right; padding: 10px;">
        <el-button type="success" icon="el-icon-check" :loading="false" round>Consultar</el-button>
      </el-col>
    </el-row>

    <!-- you can add element-ui's tooltip -->
    <el-tooltip placement="top" content="subir">
      <back-to-top
        :custom-style="myBackToTopStyle"
        :visibility-height="300"
        :back-position="50"
        transition-name="fade"
      />
    </el-tooltip>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import BackToTop from '@/components/BackToTop'

export default {
  name: 'ViewIndicesDane',
  components: { BackToTop },
  data() {
    return {
      myBackToTopStyle: {
        right: '50px',
        bottom: '50px',
        width: '40px',
        height: '40px',
        'border-radius': '4px',
        'line-height': '45px',
        background: '#e7eaf1'
      },
      optionsAno: [
        {
          value: '2007',
          label: '2007'
        },
        {
          value: '2008',
          label: '2008'
        },
        {
          value: '2009',
          label: '2009'
        },
        {
          value: '2010',
          label: '2010'
        },
        {
          value: '2011',
          label: '2011'
        },
        {
          value: '2012',
          label: '2012'
        },
        {
          value: '2013',
          label: '2013'
        },
        {
          value: '2014',
          label: '2014'
        },
        {
          value: '2015',
          label: '2015'
        },
        {
          value: '2016',
          label: '2016'
        },
        {
          value: '2017',
          label: '2017'
        },
        {
          value: '2018',
          label: '2018'
        },
        {
          value: '2019',
          label: '2019'
        }
      ],
      optionsMes: [
        {
          value: '1',
          label: 'Enero'
        },
        {
          value: '2',
          label: 'Febrero'
        },
        {
          value: '3',
          label: 'Marzo'
        },
        {
          value: '4',
          label: 'Abril'
        },
        {
          value: '5',
          label: 'Mayo'
        },
        {
          value: '6',
          label: 'Junio'
        },
        {
          value: '7',
          label: 'Julio'
        },
        {
          value: '8',
          label: 'Agosto'
        },
        {
          value: '9',
          label: 'Septiembre'
        },
        {
          value: '10',
          label: 'Octubre'
        },
        {
          value: '11',
          label: 'Noviembre'
        },
        {
          value: '12',
          label: 'Diciembre'
        }
      ],
      optionsEmpresa: [
        {
          value: '2103',
          label: 'CODENSA SA'
        },
        {
          value: '2249',
          label: 'ELECTRIFICADORA DEL CARIBE SA'
        },
        {
          value: '204',
          label: 'ELECTRIFICADORA DEL META SA'
        }
      ],
      optionsMercado: [
        {
          value: '0',
          label: 'Opción 1'
        },
        {
          value: '1',
          label: 'Opción 2'
        },
        {
          value: '2',
          label: 'Opción 3'
        }
      ],
      value1: '',
      value2: '',
      value3: '',
      value4: ''
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {}
}
</script>

<style lang="scss" scoped>
	.placeholder-container div {
		margin: 10px;
	}
</style>
