<template>
  <div>
    <el-card class="box-card margin-card" style="border: 2px solid #C0C4CC; height: 78vh;">
      <div slot="header" class="clearfix">
        <el-row>
          <el-col :span="18">
            <el-row style="padding-bottom: 0.5em;">
              <el-col style="text-align: right;" :span="3"><b>Año:</b></el-col>
              <el-col style="padding-left: 1em;" :span="21">{{ msgviewparent.ano }}</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5em;">
              <el-col style="text-align: right;" :span="3"><b>Mes:</b></el-col>
              <el-col style="padding-left: 1em;" :span="21">{{ getMes(msgviewparent.mes) }}</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5em;">
              <el-col style="text-align: right;" :span="3"><b>Tolerancia:</b></el-col>
              <el-col style="padding-left: 1em;" :span="21">{{ tolerancia }}</el-col>
            </el-row>
          </el-col>
          <el-col :span="5" style="padding-top: 2em;">
            <el-input v-model="search" size="mini" placeholder="Buscar" />
          </el-col>
        </el-row>
      </div>
      <el-table
        v-loading="loading"
        :default-sort="{prop: 'id_mercado', order: 'ascending'}"
        :data="tableData.filter(data => !search || data.mercado.toLowerCase().includes(search.toLowerCase()))"
        :border="true"
        style="width: 100%;"
        height="60vh"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" align="center" />
        <el-table-column prop="id_mercado" label="ID Mercado" width="125" align="center" sortable />
        <el-table-column prop="mercado" label="Mercado" width="180" align="center" sortable />
        <el-table-column prop="nt_prop" label="NT - PROP" width="130" align="center" sortable />
        <el-table-column
          v-for="column in colComponentes"
          :key="column.label"
          :label="column.label"
          :prop="column.prop"
          align="center"
        >
          <el-table-column
            prop="tarifa"
            label="Tarifa m"
            align="center"
          >
            <template slot-scope="scope">
              <!-- {{ scope.row }} -->
              <!-- {{ column.prop }} -->
              <div v-for="tarifa in scope.row.tarifas[0][column.prop]" :key="tarifa.value">
                <el-popover placement="top-start" width="315" trigger="hover" popper-class="popover-cpte" visible-arrow="false">
                  <div class="text_popover">Tarifarito informa</div>
                  <div style="padding-top: 1em; text-align: center;">
                    <label>{{ tarifa.label_anterior }}</label>
                    <span>&nbsp;${{ tarifa.tarifa_mes_anterior.toFixed(5) }}</span>
                  </div>
                  <div style="padding-top: 1em; text-align: center;">
                    <label>{{ tarifa.label_publicado }}</label>
                    <span>&nbsp;${{ tarifa.tarifa_publicada.toFixed(5) }}</span>
                  </div>
                  <div style="text-align: center;">
                    <label>{{ tarifa.label_calculado }}</label>
                    <span>&nbsp;${{ tarifa.tarifa_calculada.toFixed(5) }}</span>
                  </div>
                  <div style="text-align: center;">
                    <label>Diferencia:</label>
                    <span
                      v-if="parseFloat(tarifa.tarifa_publicada - tarifa.tarifa_calculada).toFixed(5) == 0"
                    >$0</span>
                    <span
                      v-else-if="parseFloat(tarifa.tarifa_publicada - tarifa.tarifa_calculada).toFixed(5) != 0"
                    >${{ parseFloat(tarifa.tarifa_publicada - tarifa.tarifa_calculada).toFixed(5) }}</span>
                  </div>
                  <el-button
                    v-if="(tarifa.tarifa_publicada - tarifa.tarifa_calculada >= 0
                      && tarifa.tarifa_publicada - tarifa.tarifa_calculada <= tolerancia)
                      || (tarifa.tarifa_publicada - tarifa.tarifa_calculada < 0
                      && tarifa.tarifa_publicada - tarifa.tarifa_calculada >= -tolerancia)"
                    slot="reference"
                    type="success"
                    icon="el-icon-check"
                    circle
                    @click="handleClickComponent(scope.$index, scope.row, tarifa.value)"
                  />
                  <el-button
                    v-else-if="(tarifa.tarifa_publicada - tarifa.tarifa_calculada < 0
                      && tarifa.tarifa_publicada - tarifa.tarifa_calculada <= -tolerancia)"
                    slot="reference"
                    type="warning"
                    icon="el-icon-check"
                    circle
                    @click="handleClickComponent(scope.$index, scope.row, tarifa.value)"
                  />
                  <el-button
                    v-else
                    slot="reference"
                    type="danger"
                    icon="el-icon-close"
                    circle
                    @click="handleClickComponent(scope.$index, scope.row, componente.value)"
                  />
                </el-popover>
              </div>
            </template>
          </el-table-column>
          <el-table-column
            v-if="column.prop === 'Estrato 1' || column.prop === 'Estrato 2' || column.prop === 'Estrato 3'"
            prop="subsidio"
            label="%Sub m"
            align="center"
          >
            <template slot-scope="scope">
              <!-- {{ scope.row.tarifas[0][column.prop] }} -->
              <div v-for="tarifa in scope.row.tarifas[0][column.prop]" :key="tarifa.value">
                <el-popover v-if="tarifa.value === 'estrato1' || tarifa.value === 'estrato2' || tarifa.value === 'estrato3'" placement="top-start" width="315" trigger="hover" popper-class="popover-cpte" visible-arrow="false">
                  <div class="text_popover">Tarifarito informa</div>
                  <div style="padding-top: 1em; text-align: center;">
                    <label>{{ tarifa.lbl_porcen_publicado }}</label>
                    <span>&nbsp;{{ tarifa.por_subsidio_publicado.toFixed(2) }}%</span>
                  </div>
                  <div style="text-align: center;">
                    <label>{{ tarifa.lbl_porcen_calculado }}</label>
                    <span>&nbsp;{{ tarifa.por_subsidio_calculado.toFixed(2) }}%</span>
                  </div>
                  <div style="text-align: center;">
                    <label>Diferencia:</label>
                    <span
                      v-if="parseFloat(tarifa.por_subsidio_publicado - tarifa.por_subsidio_calculado).toFixed(2) == 0"
                    >0%</span>
                    <span
                      v-else-if="parseFloat(tarifa.por_subsidio_publicado - tarifa.por_subsidio_calculado).toFixed(2) != 0"
                    >{{ parseFloat(tarifa.por_subsidio_publicado - tarifa.por_subsidio_calculado).toFixed(2) }}%</span>
                  </div>
                  <el-button
                    v-if="(tarifa.por_subsidio_publicado - tarifa.por_subsidio_calculado >= 0
                      && tarifa.por_subsidio_publicado - tarifa.por_subsidio_calculado <= tolerancia)
                      || (tarifa.por_subsidio_publicado - tarifa.por_subsidio_calculado < 0
                      && tarifa.por_subsidio_publicado - tarifa.por_subsidio_calculado >= -tolerancia)"
                    slot="reference"
                    type="success"
                    icon="el-icon-check"
                    circle
                    @click="handleClickComponent(scope.$index, scope.row, tarifa.value)"
                  />
                  <el-button
                    v-else-if="(tarifa.por_subsidio_publicado - tarifa.por_subsidio_calculado < 0
                      && tarifa.por_subsidio_publicado - tarifa.por_subsidio_calculado <= -tolerancia)"
                    slot="reference"
                    type="warning"
                    icon="el-icon-check"
                    circle
                    @click="handleClickComponent(scope.$index, scope.row, tarifa.value)"
                  />
                  <el-button
                    v-else
                    slot="reference"
                    type="danger"
                    icon="el-icon-close"
                    circle
                    @click="handleClickComponent(scope.$index, scope.row, componente.value)"
                  />
                </el-popover>
              </div>
            </template>
          </el-table-column>
        </el-table-column>
      </el-table>
    </el-card>

    <el-row :gutter="10" class="footer">
      <el-col :sm="24" :md="21" class="cont-btn" style="text-align: right;">
        <el-tooltip
          class="item hidden-sm-and-down"
          effect="dark"
          content="Se cerrará la verificación de los componentes que no superaron los niveles de tolerancia establecidos."
          placement="top-start"
        >
          <i class="el-icon-info" style="color: #304156;" />
        </el-tooltip>
        <el-button type="primary" class="btnVerify" @click="functionConfirmar">Verificación en lote</el-button>
      </el-col>
      <el-col :sm="24" :md="3">
        <el-button class="btn" @click="closeViewGridCu">Cancelar</el-button>
      </el-col>
    </el-row>

    <!-- Se carga la vista del componente seleccionado -->
    <el-dialog
      :title="modulo"
      :before-close="handleClose"
      :visible.sync="viewCpteVisible"
      fullscreen
      append-to-body
      destroy-on-close
      custom-class="dialog-component"
      @close="closeViewComponent"
    >
      <component :is="currentView" :messagecomponent="componentSelect" @clicked="onClickChild" />
    </el-dialog>
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css'
import { mapGetters } from 'vuex'
import logTarifarito from '../../../../../../assets/logo_buho.png'
// import viewG from './component-g.vue'
// import viewT from './component-t.vue'
// import ViewP from './component-p'
// import viewDtun from './component-dtun.vue'
// import viewR from './component-r.vue'
// import viewC from './component-c.vue'
// import viewCu from './component-cu.vue'
import componentsTable from '../options/componentsTable'
import { getNToleranciaMes } from '@/api/tarifarito/gestor/nTolerancia'

import { CONSTANTS } from '../../../../../../constants/constants'

export default {
  closename: 'ViewGridCu',
  components: {
    // viewG,
    // viewT,
    // ViewP,
    // viewDtun,
    // viewR,
    // viewC,
    // viewCu
  },
  props: {
    msgviewparent: {
      type: Object,
      default: function() {
        return { Component: null }
      }
    }
  },
  data() {
    return {
      modulo: null,
      currentView: null,
      logo: logTarifarito,
      tableData: componentsTable,
      multipleSelection: [],
      loading: false,
      search: '',
      viewCpteVisible: false,
      optionsMes: CONSTANTS.optionsMes,
      value_ano: '',
      value_mes: '',
      cod_empresa: '',
      nombre_empresa: '',
      dialogComponentP: false,
      radioCreg: '',
      componentSelect: {},
      colComponentes: '',
      tolerancia: 0.5
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    this.initView()
  },
  methods: {
    async initView() {
      console.log('DATAPARENT -> ', this.msgviewparent)
      this.tableData = this.msgviewparent.data
      this.createColCptes()
      this.nombre_empresa = this.msgviewparent.empresa
      this.value_ano = this.msgviewparent.ano
      this.value_mes = this.msgviewparent.mes
      await getNToleranciaMes(this.value_ano, this.value_mes).then((response) => {
        this.tolerancia = response[0].n_tolerancia
      })
    },
    createColCptes() {
      // console.log('this.tableData > ', this.tableData[0]['tarifas'][0])
      const columnComponents = []
      for (const key in this.tableData[0]['tarifas'][0]) {
        // const cpte = key.split('_')[1].toUpperCase()
        columnComponents.push({ label: key, prop: key })
      }
      this.colComponentes = columnComponents
    },
    handleClickComponent(index, row, component) {
      row.ano = this.value_ano
      row.mes = this.value_mes
      row.nombre_empresa = this.nombre_empresa
      console.log('Componente seleccionado -> ', row)
      this.componentSelect = row // Valores que se envian a la vista del componente
      if (component === 'G') {
        this.modulo = `${this.nombre_empresa} |	${row.mercado} | NTPROP ${row.nt_prop} | Módulo generación`
        this.currentView = 'viewG'
        this.viewCpteVisible = true
      }
      if (component === 'T') {
        this.modulo = `${this.nombre_empresa} |	${row.mercado} | NTPROP ${row.nt_prop} | Módulo transmisión`
        this.currentView = 'viewT'
        this.viewCpteVisible = true
      }
      if (component === 'P015' || component === 'P097') {
        this.handleSelectComponentP(component, row.mercado, row.nt_prop)
      }
      if (component === 'DTUN') {
        this.modulo = `${this.nombre_empresa} |	${row.mercado} | NTPROP ${row.nt_prop} | Componente DTUN`
        this.currentView = 'viewDtun'
        this.viewCpteVisible = true
      }
      if (component === 'R') {
        this.modulo = `${this.nombre_empresa} |	${row.mercado} | NTPROP ${row.nt_prop} | Módulo restricciones`
        this.currentView = 'viewR'
        this.viewCpteVisible = true
      }
      if (component === 'C') {
        this.modulo = `${this.nombre_empresa} |	${row.mercado} | NTPROP ${row.nt_prop} | Módulo comercialización`
        this.currentView = 'viewC'
        this.viewCpteVisible = true
      }
      if (component === 'CU') {
        this.modulo = `${this.nombre_empresa} |	${row.mercado} | NTPROP ${row.nt_prop} | Módulo CU`
        this.currentView = 'viewCu'
        this.viewCpteVisible = true
      }
    },
    handleSelectComponentP(cpte, mercado, nt_prop) {
      if (cpte === 'P015') {
        this.modulo = `${this.nombre_empresa} |	${mercado} | NTPROP ${nt_prop} | Módulo pérdidas CREG 015`
        this.currentView = 'ViewP'
        this.viewCpteVisible = true
      } else if (cpte === 'P097') {
        this.modulo = `${this.nombre_empresa} |	${mercado} | NTPROP ${nt_prop} | Módulo pérdidas CREG 097`
        this.currentView = 'ViewP'
        this.viewCpteVisible = true
      }
    },
    functionConfirmar() {
      console.log('Verificación en lote!')
    },
    getMes(value) {
      if (value) {
        const mes = this.optionsMes.find(element => element.value === value)
          .label
        return mes
      }
    },
    handleSelectionChange(val) {
      console.log(val)
      this.multipleSelection = val
    },
    handleClose(done) {
      this.$confirm('¿Realmente deseas cerrar la ventana?')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    closeViewComponent() {
      this.currentView = null
      console.log('Se cerro vista de componente!')
    },
    closeViewGridCu() {
      this.$emit('clicked', false)
    },
    onClickChild(value) {
      console.log('onClickChildComponent: ', value) // someValue
      this.viewCpteVisible = value
      this.currentView = null
    }
  }
}
</script>

<style lang="scss">
	// .dialog-component .el-dialog__header {
	// 	padding-left: 5em;
	// 	background-image: url("../../../../../../assets/logo_buho.png");
	// 	background-repeat: no-repeat;
	// 	background-size: 38px 42px;
	// 	background-position-x: 1.5em;
	// 	background-position-y: 0.5em;
	// }

	// .dialog-class {
	// 	border-radius: 10px;
	// }

	// .dialog-class .el-dialog__header {
	// 	border-radius: 10px 10px 0px 0px;
	// 	background-image: url("../../../../../../assets/logo_buho.png");
	// 	padding-left: 3.7em;
	// 	background-repeat: no-repeat;
	// 	background-size: 30px 35px;
	// 	background-position-x: 1em;
	// 	background-position-y: 0.8em;
	// }

	// .el-dialog {
	// 	background-color: #f2f6fc;
	// }

	// .el-dialog__headerbtn .el-dialog__close {
	// 	color: white;
	// }

	// .el-dialog__header {
	// 	background-color: #304156;
	// 	padding-bottom: 1em;
	// 	// border-radius: 20px;
	// }

	// .el-dialog__title {
	// 	font-weight: bold;
	// 	color: white;
	// 	margin-left: 0.5%;
	// }

	// .el-dialog__body {
	// 	padding-top: 1%;
	// 	padding-left: 3%;
	// 	padding-right: 3%;
	// }

	// .cell {
	// 	color: black;
	// }

  // .popover-cpte {
  //   color: black;
  //   background-color: #e3f2fd;
  //   border: 2px solid #4a148c;
  // }

  // .popover-cpte[x-placement^=top] .popper__arrow:after {
  //   border-top-color:#4a148c;
  // }

	// .text_popover {
	// 	text-align: center;
	// 	font-weight: bold;
	// 	font-size: 125%;
	// 	padding-bottom: 1%;
	// 	border-bottom: 1px solid;
  //   background-image: url("../../../../../../assets/logo_buho.png");
  //   padding-left: 1.2em;
	// 	background-repeat: no-repeat;
	// 	background-size: 30px 35px;
	// 	background-position-x: 1em;
	// 	background-position-y: 0.5em;
	// }

	// // Pantallas superiores a 800px (PC)
	// @media screen and (min-width: 800px) {
	// 	.size-aside-md {
	// 		margin-left: 1.5em;
	// 	}

	// 	.cont-btn {
	// 		text-align: right;
	// 	}

	// 	.btnVerify {
	// 		width: 12em;
	// 	}
	// }

	// // Pantallas inferiores a 800px (mobile)
	// @media screen and (max-width: 800px) {
	// 	.cont-btn {
	// 		padding-bottom: 0.5em;
	// 	}

	// 	.btnVerify {
	// 		width: 100%;
	// 	}
	// }
</style>
