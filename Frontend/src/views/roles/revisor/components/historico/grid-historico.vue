<template>
  <div>
    <el-card v-loading="loading" class="box-card margin-card" style="border: 2px solid #C0C4CC; height: 78vh;">
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
        v-if="!loading"
        :default-sort="{prop: 'fecha_modif', order: 'descending'}"
        :data="tableData.filter(data => !search || data.fecha_modif.toLowerCase().includes(search.toLowerCase()))"
        :border="false"
        style="width: 100%;"
        height="60vh"
      >
        <el-table-column prop="fecha_modif" label="Modificación" align="center" sortable />
        <el-table-column prop="nom_empresa" label="Nombre Empresa" width="300" align="center" sortable />
        <el-table-column prop="nom_mercado" label="Mercado" align="center" sortable />
        <el-table-column prop="componente" label="Componente" align="center" sortable />
        <el-table-column prop="nt_prop" label="NT - PROP" align="center" sortable />
        <el-table-column prop="usuario" label="Usuario" align="center" sortable />
        <el-table-column prop="estado" label="Estado" align="center" sortable>
          <template slot-scope="scope">
            <div>
              <span v-if="scope.row.estado === 'En gestión'" style="color: #ff9800;">En gestión&nbsp;<i class="el-icon-loading" /></span>
              <span v-if="scope.row.estado === 'Verificado'" style="color: #00c853;">Verificado&nbsp;<i class="el-icon-circle-check" /></span>
            </div>
          </template>
        </el-table-column>
        <el-table-column
          label="Detalle"
          align="center"
        >
          <template slot-scope="scope">
            <div style="text-align: center;">
              <el-button
                size="small"
                type="success"
                icon="el-icon-search"
                @click="detalleComponente(scope.$index, scope.row)"
              >Ver</el-button>
            </div>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-row :gutter="10" class="footer">
      <el-col :sm="24" :md="24" style="text-align: right; padding-right: 3em;">
        <el-button class="btn" type="primary" @click="closeViewGridHistorico">Regresar</el-button>
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
      <component :is="currentView" :messagehistory="componentSelect" @clicked="onClickChild" />
    </el-dialog>
  </div>
</template>

<script>
// import 'element-ui/lib/theme-chalk/display.css'
import { mapGetters } from 'vuex'
import { Message } from 'element-ui'
import { getNToleranciaMes } from '@/api/tarifarito/gestor/nTolerancia'
import gridComponente from './grid-componente'
import { CONSTANTS } from '../../../../../constants/constants'
import { getComponentes } from '@/api/tarifarito/revisor/historico/componentes_cu'

export default {
  closename: 'ViewGridHistorico',
  components: {
    gridComponente
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
      multipleSelection: [],
      loading: true,
      search: '',
      viewCpteVisible: false,
      optionsMes: CONSTANTS.optionsMes,
      tableData: [],
      value_ano: '',
      value_mes: '',
      cod_empresa: '',
      nom_empresa: '',
      dialogComponentP: false,
      radioCreg: '',
      componentSelect: {},
      colComponentes: CONSTANTS.columnComponents,
      tolerancia: null
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
      this.nom_empresa = this.msgviewparent.empresa
      this.value_ano = this.msgviewparent.ano
      this.value_mes = this.msgviewparent.mes
      this.value_empresa = this.msgviewparent.cod_empresa
      this.value_mercado = this.msgviewparent.cod_mercado
      await getNToleranciaMes(this.value_ano, this.value_mes).then((response) => {
        console.log('TOLERANCIA --> ', response)
        this.tolerancia = response[0].n_tolerancia
      }, (err) => {
        console.log(err)
      })
      this.getDataComponent()
    },
    async getDataComponent() {
      await getComponentes(
        this.value_ano,
        this.value_mes,
        this.value_empresa,
        this.value_mercado
      ).then(response => {
        console.log('RESPONSE -> ', response)
        if (response.length > 0) {
          console.log('setDataComponentes -> ', response)
          this.tableData = response
          this.loading = false
        } else {
          Message({
            message: 'No hay información para los criterios seleccionados',
            type: 'warning',
            duration: 5 * 1000
          })
          this.closeViewComponent()
          this.closeViewGridHistorico()
        }
      // eslint-disable-next-line handle-callback-err
      }, (err) => {
        Message({
          message: 'No se pudo completar la operación.',
          type: 'error',
          duration: 5 * 1000
        })
        // this.loading = false
      })
    },
    detalleComponente(index, row) {
      console.log('COMPONENTE SELECCIONADO -> ', row)
      this.componentSelect = row // Valores que se envian a la vista del componente
      const component = row.componente
      if (component === 'G') {
        this.modulo = `${this.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo generación`
      }
      if (component === 'T') {
        this.modulo = `${this.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo transmisión`
      }
      if (component === 'P015' || component === 'P097') {
        this.handleSelectComponentP(component, row.nom_mercado, row.nt_prop)
      }
      if (component === 'DTUN') {
        this.modulo = `${this.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Componente DTUN`
      }
      if (component === 'R') {
        this.modulo = `${this.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo restricciones`
      }
      if (component === 'C') {
        this.modulo = `${this.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo comercialización`
      }
      if (component === 'CU') {
        this.modulo = `${this.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo CU`
      }
      this.currentView = 'gridComponente'
      this.viewCpteVisible = true
    },
    handleSelectComponentP(cpte, mercado, nt_prop) {
      if (cpte === 'P015') {
        this.modulo = `${this.nom_empresa} |	${mercado} | NTPROP ${nt_prop} | Módulo pérdidas CREG 015`
      } else if (cpte === 'P097') {
        this.modulo = `${this.nom_empresa} |	${mercado} | NTPROP ${nt_prop} | Módulo pérdidas CREG 097`
      }
      this.currentView = 'gridComponente'
      this.viewCpteVisible = true
    },
    getMes(value) {
      if (value) {
        const mes = this.optionsMes.find(element => element.value === value).label
        return mes
      }
    },
    handleSelectionChange(val) {
      // console.log(val)
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
    closeViewGridHistorico() {
      this.$emit('clicked', false)
    },
    onClickChild(value) {
      console.log('onClickChildComponent_gridhistorico: ', value) // someValue
      this.viewCpteVisible = false
      this.currentView = null
      this.loading = true
      this.tableData = []
      this.initView()
    }
  }
}
</script>

<style lang="scss">
	.dialog-component .el-dialog__header {
		padding-left: 5em;
		background-image: url('../../../../../assets/logo_buho.png');
		background-repeat: no-repeat;
		background-size: 38px 42px;
		background-position-x: 1.5em;
		background-position-y: 0.5em;
	}

	.dialog-class {
		border-radius: 10px;
	}

	.dialog-class .el-dialog__header {
		border-radius: 10px 10px 0px 0px;
		background-image: url('../../../../../assets/logo_buho.png');
		padding-left: 3.7em;
		background-repeat: no-repeat;
		background-size: 30px 35px;
		background-position-x: 1em;
		background-position-y: 0.8em;
	}

	.el-dialog {
		background-color: #f2f6fc;
	}

	.el-dialog__headerbtn .el-dialog__close {
		color: white;
	}

	.el-dialog__header {
		background-color: #304156;
		padding-bottom: 1em;
		// border-radius: 20px;
	}

	.el-dialog__title {
		font-weight: bold;
		color: white;
		margin-left: 0.5%;
	}

	.el-dialog__body {
		padding-top: 1%;
		padding-left: 3%;
		padding-right: 3%;
	}

	.cell {
		color: black;
	}

  .popover-cpte {
    color: black;
    background-color: #e3f2fd;
    border: 2px solid #4a148c;
  }

  .popover-cpte[x-placement^=top] .popper__arrow:after {
    border-top-color:#4a148c;
  }

	.text_popover {
		text-align: center;
		font-weight: bold;
		font-size: 125%;
		padding-bottom: 1%;
		border-bottom: 1px solid;
    background-image: url('../../../../../assets/logo_buho.png');
    padding-left: 1.2em;
		background-repeat: no-repeat;
		background-size: 30px 35px;
		background-position-x: 1em;
		background-position-y: 0.5em;
	}

	// Pantallas superiores a 800px (PC)
	@media screen and (min-width: 800px) {
		.size-aside-md {
			margin-left: 1.5em;
		}

		.cont-btn {
			text-align: right;
		}

		.btnVerify {
			width: 12em;
		}
	}

	// Pantallas inferiores a 800px (mobile)
	@media screen and (max-width: 800px) {
		.cont-btn {
			padding-bottom: 0.5em;
		}

		.btnVerify {
			width: 100%;
		}
	}
</style>
