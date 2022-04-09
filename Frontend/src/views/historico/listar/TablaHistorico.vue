<template>
  <!-- Tabla donde se lista, ordena y realiza busqueda de los expedientes -->
  <div class="app-container" style="height: auto;">
    <el-card class="box-card">
      <el-row :gutter="10" class="filter-container">
        <el-col :xs="12" :md="2">
          <el-select v-model="listQuery.anio" size="small" :filterable="x.matches ? false : true" placeholder="Año" :clearable="false" style="width: 100%;" class="filter-item">
            <el-option v-for="item in anioOptions" :key="item" :label="item" :value="item" />
          </el-select>
        </el-col>
        <el-col :xs="12" :md="5" style="border: 0px solid red;">
          <el-input v-model="listQuery.expediente" size="small" placeholder="Expediente" :clearable="false" style="width: 100%;" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :xs="12" :md="6" style="border: 0px solid red;">
          <el-input v-model="listQuery.nit" size="small" placeholder="Nit empresa" :clearable="false" style="width: 100%;" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
        <el-col :xs="12" :md="11" style="border: 0px solid red;">
          <el-input v-model="listQuery.norma" size="small" placeholder="Norma infringida" :clearable="false" style="width: 100%;" class="filter-item" @keyup.enter.native="handleFilter" />
        </el-col>
      </el-row>

      <el-row :gutter="10" class="filter-container">
        <el-col :sm="24" :md="7" style="border: 0px solid red;">
          <el-select v-model="listQuery.causal" size="small" :filterable="x.matches ? false : true" placeholder="Causal" multiple collapse-tags :clearable="false" class="filter-item" style="width: 100%" @change="selectCausal($event)">
            <el-option v-for="item in selectCausalOptions" :key="item.id" :label="item.nombre" :value="item.id.toString()">
              <span style="float: left">{{ item.nombre }}&nbsp;</span>
              <!-- <span style="float: right; color: #8492a6; font-size: 13px">IDC{{ item.id }}</span> -->
            </el-option>
          </el-select>
        </el-col>
        <el-col :sm="24" :md="9" style="border: 0px solid red;">
          <el-select v-model="listQuery.subcausal" size="small" :filterable="x.matches ? false : true" placeholder="Subcausal" multiple collapse-tags :clearable="false" class="filter-item" style="width: 100%">
            <el-option v-for="item in selectSubCausalOptions" :key="item.id" :label="item.nombre" :value="convertToObj(item.id + '-' + item.idsubcausal)">
              <span style="float: left">{{ item.nombre }}&nbsp;</span>
              <!-- <span style="float: right; color: #8492a6; font-size: 13px">IDC{{ item.idcausal }}</span> -->
            </el-option>
          </el-select>
        </el-col>
        <el-col :xs="12" :md="2" style="border: 0px solid red;">
          <el-button v-waves class="filter-item" type="success" size="small" icon="el-icon-search" style="width: 100%;" @click="handleFilter">Buscar</el-button>
        </el-col>
        <el-col :xs="12" :md="2" style="border: 0px solid red;">
          <el-button v-waves class="filter-item" type="danger" size="small" icon="el-icon-remove-outline" style="width: 100%;" @click="handleRemove">Limpiar</el-button>
        </el-col>
        <el-col :xs="12" :md="2">
          <el-button v-waves :loading="downloadGeneral" class="filter-item" type="primary" icon="el-icon-download" size="small" style="width: 100%;" @click="downloadExcelGeneral">Info General</el-button>
        </el-col>
        <el-col :xs="12" :md="2">
          <el-button v-waves :loading="downloadEspecifica" class="filter-item" type="primary" icon="el-icon-download" size="small" style="width: 100%;" @click="downloadExcelEspecifica">Específica</el-button>
        </el-col>
      </el-row>

      <el-table v-loading="listLoading" border size="small" :data="list" :height="x.matches ? '22em' : '59vh'" style="width: 100%" class="table-historico" @selection-change="handleSelectionChange">
        <el-table-column type="expand">
          <template slot-scope="props">
            <p v-for="expand in tableexpand" :key="expand.prop" style="padding-left: 5em;">
              <span v-if="props.row[expand.prop]">
                <span v-if="expand.prop.substr(0, 2) === 'f_'">
                  <span v-if="props.row[expand.prop] != 'None'">
                    <b>{{ expand.label }}:</b> {{ convertDate(props.row[expand.prop]) }}
                  </span>
                </span>
                <span v-else-if="expand.download === true">
                  <span v-if="props.row[expand.prop]['value'] === 'NO PRESENTÓ RECURSO'">
                    <b>{{ expand.label }}:</b> No presentó recurso
                  </span>
                  <span v-else-if="props.row[expand.prop]['value'] !== null">
                    <b>{{ expand.label }}:</b> <el-link type="primary" style="font-size: small;" @click="download(props.row[expand.prop]['value'])"><ins>{{ props.row[expand.prop]['value'].split('/')[3] }}</ins></el-link>
                  </span>
                </span>
                <span v-else-if="expand.prop === 'valor_sancion_recurso' || expand.prop === 'valor_sancion'">
                  <b>{{ expand.label }}:</b> $ {{ props.row[expand.prop] | toThousandFilter }}
                </span>
                <span v-else-if="expand.prop === 'cargos'">
                  <span v-if="props.row[expand.prop].length > 0">
                    <el-link type="primary" style="font-size: small;" @click="openModalCargos(props.row[expand.prop])"><ins>{{ expand.label }}</ins></el-link>
                  </span>
                </span>
                <span v-else>
                  <b>{{ expand.label }}:</b> {{ props.row[expand.prop] }}
                </span>
              </span>
            </p>
          </template>
        </el-table-column>
        <el-table-column
          v-for="column in tablecolumns"
          :key="column.label"
          :label="column.label"
          :prop="column.prop"
          :align="column.align"
          :sortable="column.sortable"
          :width="column.width"
        >
          <template slot-scope="scope">
            <div v-if="column.prop.substr(0, 2) === 'f_'"><i v-show="convertDate(scope.row[column.prop]) === 'No aplica' ? false : true" class="el-icon-time" /> {{ convertDate(scope.row[column.prop]) }}</div>
            <div v-else-if="column.prop === 'n_empresa'" class="keepAll">{{ scope.row[column.prop] }}</div>
            <div v-else-if="column.prop === 'nit_empresa'">{{ getCheckDigit(scope.row[column.prop]) }}</div>
            <!-- columna donde se cargan las causas / subcausales -->
            <span v-else-if="column.prop === 'causas' || column.prop === 'subcausales'">
              <span v-if="scope.row[column.prop].length">
                <span v-for="(causa, index) in scope.row[column.prop]" :key="column.prop === 'subcausales' ? causa.id : causa.idcausa">
                  <div v-if="scope.row[column.prop].length > 1" style="border-top: 1px solid #E4E7ED; padding-top: 6px; padding-bottom: 6px;" :style="(index + 1) === scope.row[column.prop].length ? {borderBottom:'1px solid #E4E7ED'}: {}">
                    <el-tag type="primary">{{ causa.nombre }}</el-tag>
                  </div>
                  <div v-else>
                    <p>
                      <el-tag type="primary">{{ causa.nombre }}</el-tag>
                    </p>
                  </div>
                </span>
              </span>
              <span v-else>
                <el-tag type="info">No aplica</el-tag>
              </span>
            </span>
            <div v-else>{{ scope.row[column.prop] }}</div>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <pagination v-show="total>0" small :layout="x.matches ? 'prev, pager, next' : 'total, sizes, prev, pager, next, jumper'" style="padding-top: 0;" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <!-- Cuadro de dialogo para mostrar PDF's -->

    <ModalPdf
      :modalvisible="dialogVisible"
      :srcparam="urlPdf"
      @closeModalPdf="closeModalPdf"
    />

    <!-- Cuadro de dialogo para mostrar cargos -->

    <ModalCargos
      :modalvisible="dialogCargosVisible"
      :datacargos="dataCargos"
      @closeModalCargos="closeModalCargos"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import moment from 'moment'
import waves from '@/directive/waves' // waves directive
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import { getHistoricoGeneral, getHistoricoEspecifico, getAniosHistorico } from '@/api/procesosDIEG/historico'
import { getListCausal } from '@/api/procesosDIEG/causal'
import { getListSubCausal } from '@/api/procesosDIEG/subcausal'
import ModalPdf from '@/components/ModalPdf'
import ModalCargos from './ModalCargos'
import { CONSTANTS } from '../constants/constants'

const selectCausalOptions = []
const selectSubCausalOptions = []

export default {
  name: 'TablaHistorico',
  components: { Pagination, ModalPdf, ModalCargos },
  directives: { waves },
  props: {
    tablecolumns: {
      type: Array,
      default: null
    },
    tabledata: {
      type: Array,
      default: null
    },
    tableexpand: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      dataCargos: [],
      dialogCargosVisible: false,
      dialogVisible: false,
      showReviewer: false,
      list: null,
      listQuery: {
        page: 1,
        limit: 30,
        anio: undefined,
        expediente: undefined,
        nit: undefined,
        formatNit: undefined,
        causal: [],
        subcausal: [],
        norma: undefined,
        normas: undefined
      },
      anioOptions: [],
      selectCausalOptions,
      selectSubCausalOptions,
      total: 0,
      listLoading: true,
      showOnlyAdmin: false,
      datosProcesos: [],
      busquedaExpediente: '',
      filters: {},
      urlPdf: undefined,
      x: '',
      options: [],
      value: [],
      listRemote: [],
      loading: false,
      states: CONSTANTS.arrrayRemote,
      downloadGeneral: false,
      downloadEspecifica: false,
      filename: '',
      listGeneral: [],
      api: process.env.VUE_APP_BASE_API
    }
  },
  computed: {
    ...mapGetters(['sidebar', 'name', 'roles', 'usuario', 'idusuario', 'dependencia'])
  },
  created() {
    this.getHistoricoAnios()
    this.toggleSideBar()
    this.getList()
    this.getCausales()
    this.getSubCausales()
    this.x = window.matchMedia('(max-width: 800px)')
  },
  destroyed() {
    if (!this.sidebar.opened && !this.x.matches) { // Si el sidebar esta cerrado se abre
      this.$store.dispatch('app/toggleSideBar')
    }
  },
  methods: {
    async getHistoricoAnios() {
      await getAniosHistorico().then(response => {
        this.anioOptions = response
      })
    },
    downloadExcelGeneral() {
      this.downloadGeneral = true
      import('@/vendor/Export2Excel').then(excel => {
        const tHeader = CONSTANTS.tHeaderGeneral
        const filterVal = CONSTANTS.filterValGeneral
        const list = this.listGeneral
        const data = this.formatJson(filterVal, list)
        excel.export_json_to_excel({
          header: tHeader,
          data,
          filename: this.filename
        })
        this.downloadGeneral = false
      })
    },
    async downloadExcelEspecifica() {
      // this.downloadEspecifica = true
      await getHistoricoEspecifico(this.listQuery).then(response => {
        // console.log('Response historico Especifico --> ', response)
        import('@/vendor/Export2Excel').then(excel => {
          const tHeader = CONSTANTS.tHeaderEspecifica
          const filterVal = CONSTANTS.filterValEspecifica
          const list = response
          const data = this.formatJson(filterVal, list)
          excel.export_json_to_excel({
            header: tHeader,
            data,
            filename: this.filename
          })
        })
      })
      this.downloadEspecifica = false
    },
    formatJson(filterVal, jsonData) {
      return jsonData.map(v => filterVal.map(j => v[j]))
    },
    verifyNorma(query) {
      if (query !== undefined) {
        // Se crea expresion regular para buscar por una o varias normas
        const arrayNormas = this.listQuery.norma.toLowerCase().split(';').map((item) => { return item }).join('&')
        return arrayNormas
      }
    },
    openModalCargos(param) {
      param.sort(function(a, b) {
        if (a.numero_cargo > b.numero_cargo) {
          return 1
        }
        if (a.numero_cargo < b.numero_cargo) {
          return -1
        }
        // a must be equal to b
        return 0
      })
      this.dataCargos = param
      this.dialogCargosVisible = true
    },
    closeModalCargos() {
      this.dialogCargosVisible = false
    },
    toggleSideBar() {
      // console.log('STATUS SIDEBAR ---> ', JSON.stringify(this.sidebar))
      if (this.sidebar.opened && !this.x.matches) { // Se oculta sidebar si esta abierto
        this.$store.dispatch('app/toggleSideBar')
      }
    },
    convertToObj(params) {
      const values = params.split('-')
      const obj = { consecutivo: values[0], idsubcausal: values[1] }
      return JSON.stringify(obj)
    },
    selectCausal(param) {
      // console.log('causal select --> ', param)
      this.getSubCausales(JSON.stringify(param))
    },
    closeModalPdf() {
      this.dialogVisible = false
    },
    getCheckDigit(nit) {
      let value = null
      let lenNit = null
      value = nit.toString()
      lenNit = value.length - 1
      if (lenNit !== 0) {
        value = value.slice(0, lenNit) + '-' + value[lenNit]
      } else {
        value = 'No aplica'
      }
      return value
    },
    async getCausales() {
      await getListCausal().then((response) => {
        // console.log('this.listaCausal - > ', response)
        this.selectCausalOptions = response
      })
    },
    async getSubCausales(param) {
      await getListSubCausal(param).then((response) => {
        // console.log('this.listaSubCausal - > ', response)
        this.selectSubCausalOptions = response
      })
    },
    async getList() {
      this.listLoading = true
      await getHistoricoGeneral(this.listQuery).then(response => {
        // console.log('Response historico V2 --> ', response)
        this.list = response.data.items
        this.total = response.data.total
        this.listLoading = false

        this.listGeneral = response.data.list.map((item) => {
          for (const key in item) {
            if (key.substr(0, 2) === 'f_') {
              item[key] = item[key] !== 'None' ? new Date(moment(item[key]).format('YYYY/MM/DD HH:mm:ss')) : '' // Formateamos fechas a Date
            }
            // linea para armar el PDF
            item[key] = item[key] !== null && item[key].hasOwnProperty('download') && item[key]['value'] !== null && item[key]['value'] !== 'NO PRESENTÓ RECURSO' ? `http://${window.location.hostname}/${this.api}/historico/document?root=${item[key]['value'].split('/')[0]}&year=${item[key]['value'].split('/')[1]}&folder=${item[key]['value'].split('/')[2]}&document=${item[key]['value'].split('/')[3]}` : item[key] !== null && item[key]['value'] !== null ? item[key] : null
          }
          return item
        })
      })
    },
    handleFilter() {
      this.listQuery.formatNit = this.verifyNit(this.listQuery.nit)
      this.listQuery.normas = this.verifyNorma(this.listQuery.norma)
      // console.log('norma :>> ', this.listQuery.normas)
      this.listQuery.page = 1
      this.getList()
    },
    verifyNit(query) {
      if (query !== undefined) {
        let nit = []
        nit = this.listQuery.nit.split('-')
        if (nit[1] !== undefined) {
          nit = `${nit[0]}${nit[1]}`
        } else {
          nit = nit[0]
        }
        return nit
      }
    },
    handleRemove() {
      this.listQuery = {
        page: 1,
        limit: 30,
        anio: undefined,
        expediente: undefined,
        nit: undefined,
        formatNit: undefined,
        causal: [],
        subcausal: [],
        norma: undefined,
        normas: undefined
      }
      this.getList()
    },
    download(data) {
      const split = data.split('/')
      // linea para armar el PDF
      const pdf = `${this.api}/historico/document?root=${split[0]}&year=${split[1]}&folder=${split[2]}&document=${split[3]}`
      if (this.x.matches) { // Si es dispositivo móvil
        // linea para descargar el PDF
        window.open(pdf, '_blank')
      } else {
        this.dialogVisible = true
        this.urlPdf = pdf
      }
    },
    convertDate(val) {
      //   console.log('convertDate -> ', val)
      if (val !== 'None') {
        return moment(val).format('DD/MM/YYYY')
      } else {
        return 'No aplica'
      }
    },
    getFilters(val) {
      // console.log(this.filters[val])
      return this.filters[val]
    },
    handleSelectionChange(val) {
      // console.log(val)
      this.multipleSelection = val
    },
    /* Metodo para realizar la busqueda de los filtros ubicado en las columnas */
    filterHandler(value, row, column) {
      const property = column['property']
      let valueProperty = row[property]
      if (property === 'caducidadsancion') {
        if (valueProperty !== 'No registra') {
          valueProperty = moment(valueProperty)
            .format('DD/MM/YYYY')
            .substring(3, 10)
        }
      }
      // console.log('value -> ', value, ' row -> ', valueProperty, ' column -> ', property)
      return valueProperty === value
    }
  }
}
</script>

<style lang="scss">
  /* width */
  .table-historico ::-webkit-scrollbar {
    width: 4px;
    height: 8px;
  }

  /* Track */
  .table-historico ::-webkit-scrollbar-track {
    background: #f1f1f1;
  }

  /* Handle */
  .table-historico ::-webkit-scrollbar-thumb {
    background: #C0C4CC;
  }

  /* Handle on hover */
  .table-historico ::-webkit-scrollbar-thumb:hover {
    background: #555;
  }

  // Pantallas inferiores a 800px (mobile)
  @media screen and (max-width: 800px) {
    .el-select-dropdown {
      left: 0 !important;
    }
  }

</style>
