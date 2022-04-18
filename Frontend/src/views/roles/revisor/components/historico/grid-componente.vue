<template>
  <div>
    <el-card v-loading="loading" class="box-card margin-card" style="border: 2px solid #C0C4CC; height: 78vh;">
      <div slot="header" class="clearfix">
        <el-row>
          <el-col :span="18">
            <el-row style="padding-bottom: 0.5em;">
              <el-col style="text-align: right;" :span="3"><b>Año:</b></el-col>
              <el-col style="padding-left: 1em;" :span="21">{{ messagehistory.ano }}</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5em;">
              <el-col style="text-align: right;" :span="3"><b>Mes:</b></el-col>
              <el-col style="padding-left: 1em;" :span="21">{{ getMes(messagehistory.mes) }}</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5em;">
              <el-col style="text-align: right;" :span="3"><b>Tolerancia:</b></el-col>
              <el-col style="padding-left: 1em;" :span="21">{{ tolerancia }}</el-col>
            </el-row>
            <el-row style="padding-bottom: 0.5em;">
              <el-col style="text-align: right;" :span="3"><b>Componente:</b></el-col>
              <el-col style="padding-left: 1em;" :span="21">{{ messagehistory.componente }}</el-col>
            </el-row>
            <el-row>
              <el-col style="text-align: right;" :span="3"><b>Estado actual:</b></el-col>
              <el-col style="padding-left: 1em;" :span="21">{{ messagehistory.estado }}</el-col>
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
        :data="!loading ? tableData.filter(data => !search || data.novedad.toLowerCase().includes(search.toLowerCase())) : null"
        :border="false"
        style="width: 100%;"
        height="55vh"
      >
        <el-table-column prop="fecha_modif" label="Fecha" align="center" sortable />
        <el-table-column prop="usuario" label="Usuario" align="center" sortable />
        <el-table-column prop="novedad" label="Observación" align="center" sortable />
        <el-table-column
          label="Detalle"
          align="center"
        >
          <template slot-scope="scope">
            <div style="text-align: center;">
              <el-button
                size="small"
                type="success"
                icon="el-icon-edit"
                @click="handleClickComponent(scope.$index, scope.row)"
              >Ver código</el-button>
            </div>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-row v-if="verificar" :gutter="10" class="footer">
      <el-col :sm="24" :md="21" class="cont-btn" style="text-align: right;">
        <el-tooltip
          class="item hidden-sm-and-down"
          effect="dark"
          content="Se cambia el estado a verificado"
          placement="top-start"
        >
          <i class="el-icon-info" style="color: #304156;" />
        </el-tooltip>
        <el-button class="btn" type="primary" @click="verificarCpte">Verificado</el-button>
      </el-col>
      <el-col :sm="24" :md="3">
        <el-button class="btn" @click="closeViewGridCpte">Regresar</el-button>
      </el-col>
    </el-row>

    <el-row v-if="!verificar" :gutter="10" class="footer">
      <el-col :sm="24" :md="24" style="text-align: center;">
        <el-button class="btn" type="primary" @click="closeViewGridCpte">Aceptar</el-button>
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
    >
      <component :is="currentView" :messagecomponent="componentSelect" @clicked="onClickChild" />
    </el-dialog>

    <!-- dialog mensaje revisión del componente -->
    <el-dialog
      title="Tarifarito reporta"
      :visible.sync="dialogFormNovedad"
      width="30em"
      top="10em"
      append-to-body
      destroy-on-close
      custom-class="dialog-class"
    >
      <el-card class="cont-row" style="margin-top: 1.2em;">
        <el-row>
          <el-col :sm="24" :md="24" style="text-align: left;">
            <label>Registrar novedad</label>
          </el-col>
          <el-col :sm="24" :md="24" class="input-padding">
            <el-input v-model="novedad" type="textarea" autosize placeholder="Ingresar novedad aquí" />
          </el-col>
        </el-row>
        <el-divider />
        <el-row>
          <el-col :sm="24" :md="24">
            <el-button type="success" icon="el-icon-check" class="btn" @click="registrarNovedad">Reportar</el-button>
          </el-col>
        </el-row>
      </el-card>
    </el-dialog>
  </div>
</template>

<script>
// import 'element-ui/lib/theme-chalk/display.css'
import moment from 'moment'
import { mapGetters } from 'vuex'
import { Message } from 'element-ui'
import viewG from '../../../revisor/components/costo-unitario/modules/component-g.vue'
import viewT from '../../../revisor/components/costo-unitario/modules/component-t.vue'
import ViewP from '../../../revisor/components/costo-unitario/modules/component-p'
import viewDtun from '../../../revisor/components/costo-unitario/modules/component-dtun'
import viewR from '../../../revisor/components/costo-unitario/modules/component-r.vue'
import viewC from '../../../revisor/components/costo-unitario/modules/component-c.vue'
import viewCu from '../../../revisor/components/costo-unitario/modules/component-cu.vue'
import { getNToleranciaMes } from '@/api/tarifarito/gestor/nTolerancia'
import { getDataComponente, postCpte } from '@/api/tarifarito/revisor/historico/componentes_cu'
import { CONSTANTS } from '../../../../../constants/constants'

export default {
  closename: 'ViewGridComponente',
  components: {
    viewG,
    viewT,
    ViewP,
    viewDtun,
    viewR,
    viewC,
    viewCu
  },
  props: {
    messagehistory: {
      type: Object,
      default: function() {
        return { message: null }
      }
    }
  },
  data() {
    return {
      modulo: null,
      currentView: null,
      tableData: null,
      multipleSelection: [],
      loading: true,
      search: '',
      viewCpteVisible: false,
      optionsMes: CONSTANTS.optionsMes,
      value_ano: '',
      value_mes: '',
      cod_empresa: '',
      nombre_empresa: '',
      dialogComponentP: false,
      radioCreg: '',
      componentSelect: null,
      colComponentes: CONSTANTS.columnComponents,
      tolerancia: 0.5,
      verificar: false,
      dialogFormNovedad: false,
      novedad: null
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
      console.log('ROL -> ', this.roles)
      if (this.roles[0] === 'aprobador') {
        this.verificar = true
      }
      console.log('DATAPARENT GRID COMPONENT -> ', this.messagehistory)
      await getNToleranciaMes(this.messagehistory.ano, this.messagehistory.mes).then((response) => {
        this.tolerancia = response[0].n_tolerancia
      })
      this.getHistoryCpte()
    },
    async getHistoryCpte() {
      await getDataComponente(
        this.messagehistory.ano,
        this.messagehistory.mes,
        this.messagehistory.cod_empresa,
        this.messagehistory.cod_mercado,
        this.messagehistory.componente,
        this.messagehistory.nt_prop
      ).then(response => {
        // console.log('RESPONSE -> ', response)
        if (response.length > 0) {
          console.log('getHistoryComponent -> ', response)
          this.tableData = response
          this.loading = false
        } else {
          Message({
            message: 'No hay información para los criterios seleccionados',
            type: 'warning',
            duration: 5 * 1000
          })
        }
      // eslint-disable-next-line handle-callback-err
      }, (err) => {
        Message({
          message: 'No se pudo completar la operación.',
          type: 'error',
          duration: 5 * 1000
        })
        this.loading = false
      })
    },
    handleClickComponent(index, row) {
      row.ano = this.messagehistory.ano
      row.mes = this.messagehistory.mes
      console.log('Componente seleccionado -> ', row)
      // Valores que se envian a la vista del componente
      this.componentSelect = {
        ano: Number(row.ano),
        mes: Number(row.mes),
        id_empresa: Number(row.cod_empresa),
        nombre_empresa: row.nom_empresa,
        id_mercado: Number(row.cod_mercado),
        mercado: row.nom_mercado,
        nt_prop: row.nt_prop,
        componentes: row.componentes,
        estado: row.estado,
        values: row.values
      }
      if (row.componente === 'G') {
        this.modulo = `${row.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo generación`
        this.currentView = 'viewG'
        this.viewCpteVisible = true
      }
      if (row.componente === 'T') {
        this.modulo = `${row.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo transmisión`
        this.currentView = 'viewT'
        this.viewCpteVisible = true
      }
      if (row.componente === 'P015' || row.componente === 'P097') {
        this.handleSelectComponentP(row.componente, row.mon_empresa, row.nom_mercado, row.nt_prop)
      }
      if (row.componente === 'DTUN') {
        this.modulo = `${row.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Componente DTUN`
        this.currentView = 'viewDtun'
        this.viewCpteVisible = true
      }
      if (row.componente === 'R') {
        this.modulo = `${row.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo restricciones`
        this.currentView = 'viewR'
        this.viewCpteVisible = true
      }
      if (row.componente === 'C') {
        this.modulo = `${row.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo comercialización`
        this.currentView = 'viewC'
        this.viewCpteVisible = true
      }
      if (row.componente === 'CU') {
        this.modulo = `${row.nom_empresa} |	${row.nom_mercado} | NTPROP ${row.nt_prop} | Módulo CU`
        this.currentView = 'viewCu'
        this.viewCpteVisible = true
      }
    },
    handleSelectComponentP(cpte, empresa, mercado, nt_prop) {
      if (cpte === 'P015') {
        this.modulo = `${empresa} |	${mercado} | NTPROP ${nt_prop} | Módulo pérdidas CREG 015`
        this.currentView = 'ViewP'
        this.viewCpteVisible = true
      } else if (cpte === 'P097') {
        this.modulo = `${empresa} |	${mercado} | NTPROP ${nt_prop} | Módulo pérdidas CREG 097`
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
    closeViewGridCpte() {
      this.currentView = null
      this.$emit('clicked', false)
      console.log('Se cerro vista detalle componente!')
    },
    verificarCpte() {
      this.dialogFormNovedad = true
    },
    async registrarNovedad() {
      if (this.novedad) {
        this.modelCpte = {
          usuario: this.name,
          ano: Number(this.messagehistory.ano),
          mes: Number(this.messagehistory.mes),
          cod_empresa: Number(this.messagehistory.cod_empresa),
          nom_empresa: this.messagehistory.nom_empresa,
          cod_mercado: Number(this.messagehistory.cod_mercado),
          nom_mercado: this.messagehistory.nom_mercado,
          componente: this.messagehistory.componente,
          nt_prop: this.messagehistory.nt_prop,
          novedad: this.novedad,
          fecha_modif: moment(new Date()).format('DD/MM/YYYY HH:mm:ss'),
          estado: 'Verificado',
          componentes: this.messagehistory.componentes,
          values: this.messagehistory.values
        }
        this.dialogFormNovedad = false
        // console.log('MODELO ENVIADO -> ', this.modelCpte)
        await postCpte(this.modelCpte).then(response => {
          // console.log('RESPONSE MODELO ENVIADO -> ', response)
          Message({
            message: 'Registros guardados con éxito!',
            type: 'success',
            duration: 2 * 1000
          })
          if (response) {
            this.$emit('clicked', false)
          }
        })
      } else {
        Message({
          message: 'Por favor primero ingresa la novedad',
          type: 'error',
          duration: 2 * 1000
        })
      }
    },
    onClickChild(value) {
      console.log('onClickChildComponent: ', value) // someValue
      this.viewCpteVisible = value
      this.currentView = null
      // Si se hacen cambios en cpte
      if (this.componentSelect) {
        this.initView()
        // this.verificar = true
      }
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
		background-color: red;
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
