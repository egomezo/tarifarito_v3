<template>
  <div class="div-cont">
    <el-row class="cont-row">
      <el-col :span="24">
        <aside>
          <span class="text-header">
            <b>DIRECCIÓN TÉCNICA DE GESTIÓN DE ENERGÍA</b>
          </span>
        </aside>
      </el-col>
      <el-col :span="24">
        <aside>
          <span class="text-user">
            <b>{{ name }}</b>
          </span>
        </aside>
      </el-col>
    </el-row>

    <el-card class="box-card card-header">
      <div slot="header" class="clearfix">
        <span class="text-page">
          <b>VERIFICACIÓN TARIFAS</b>
        </span>
      </div>

      <el-row class="cont-row">
        <el-col :sm="24" :md="24">
          <el-select v-model="value_ano" placeholder="Año" class="select-style" @change="verifyField($event)">
            <el-option
              v-for="item in optionsAno"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-col>
        <el-col :sm="24" :md="24" style="padding-top: 1em;">
          <el-select v-model="value_mes" placeholder="Mes" class="select-style" @change="verifyField($event)">
            <el-option
              v-for="item in optionsMes"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-col>
        <el-col :sm="24" :md="24" style="padding-top: 1em;">
          <el-select
            v-model="value_empresa"
            filterable
            placeholder="Empresa"
            class="select-style"
            popper-class="select-popper"
            :loading="loadingEmp"
            :loading-text="loadingText"
            @change="verifyField($event)"
          >
            <el-option
              v-for="item in optionsEmpresa"
              :key="item.cod_empresa"
              :label="`${item.cod_empresa} - ${item.nombre}`"
              :value="item.cod_empresa"
            />
          </el-select>
        </el-col>
      </el-row>

      <el-divider />

      <el-row :gutter="10">
        <el-col :sm="24" :md="24" style="text-align: center;">
          <el-button
            round
            :disabled="disableLoad"
            type="success"
            icon="el-icon-check"
            :loading="loading"
            class="btn"
            @click.native.prevent="verifyCU"
          >Consultar</el-button>
        </el-col>
      </el-row>
    </el-card>

    <!-- Se carga vista de parrilla de componentes CU -->

    <el-dialog
      :title="title_modulo"
      :before-close="handleClose"
      :visible.sync="dialogFormVisible"
      fullscreen
      append-to-body
      :destroy-on-close="true"
      custom-class="dialog-component"
      @close="closeModal"
    >
      <component :is="currentView" :msgviewparent="dataVerifyCu" @clicked="onClickChild" />
    </el-dialog>

    <!-- Se carga vista de loading -->

    <el-dialog
      :visible.sync="dialogLoadingVisible"
      custom-class="dialog-loading"
      center
      :destroy-on-close="true"
      :show-close="false"
      :close-on-click-modal="false"
      :close-on-press-escape="false"
    >
      <component :is="loadingView" />
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { Message } from 'element-ui'
import gridTarifas from './modules/grid-tarifas'
import PageLoading from '@/views/load-page/pageLoading'
import { CONSTANTS } from '../../../../../constants/constants'
import {
  getTarifas
} from '@/api/tarifarito/revisor/tarifas/tarifas-values'
import { getSUIEmpresasList } from '@/api/tarifarito/sui-empresas'

export default {
  name: 'ViewCostoUnitario',
  components: {
    gridTarifas,
    PageLoading
  },
  data() {
    this.getEmpresasList()
    return {
      disableLoad: true,
      dataVerifyCu: {},
      currentView: null,
      loadingView: 'PageLoading',
      loading: false,
      dialogFormVisible: false,
      dialogLoadingVisible: false,
      optionsAno: CONSTANTS.optionsAno,
      optionsMes: CONSTANTS.optionsMes,
      loadingEmp: true,
      loadingText: 'Cargando...',
      optionsEmpresa: [],
      value_ano: '',
      value_mes: '',
      value_empresa: '',
      title_modulo: ''
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  methods: {
    async getEmpresasList() {
      await getSUIEmpresasList()
        .then(result => {
          this.loadingEmp = false
          this.optionsEmpresa = JSON.parse(JSON.stringify(result))
          // CONDICIONES INICIALES - PRUEBA
          this.value_ano = 2020
          this.value_mes = 4
          // this.value_empresa = 502
          // this.value_empresa = 2103
          this.value_empresa = 564
          this.verifyField()
        })
      // eslint-disable-next-line handle-callback-err
        .catch(err => {
          this.loadingText = 'Error, recargue la página'
        })
    },
    async verifyCU() {
      this.dialogLoadingVisible = true
      this.loading = true
      this.tableData = []
      await getTarifas(
        this.value_ano,
        this.value_mes,
        this.value_empresa
      ).then(response => {
        console.log('RESPONSE -> ', response)
        if (response.length > 0) {
          console.log('verifyCU -> ', response)
          this.dataVerifyCu.ano = this.value_ano
          this.dataVerifyCu.mes = this.value_mes
          this.dataVerifyCu.cod_empresa = this.value_empresa
          this.dataVerifyCu.empresa = this.getEmpresa(this.value_empresa)
          this.dataVerifyCu.data = response
          this.title_modulo = this.getEmpresa(this.value_empresa) + ' | Consulta tarifas'
          this.dialogFormVisible = true
          this.dialogLoadingVisible = false
          this.currentView = 'gridTarifas'
        } else {
          Message({
            message: 'No hay información para el período seleccionado',
            type: 'warning',
            duration: 5 * 1000
          })
        }
      // eslint-disable-next-line handle-callback-err
      }, (err) => {
        Message({
          message: 'Revise que se hayan registrado valores desde el gestor.',
          type: 'warning',
          duration: 5 * 1000
        })
        this.loading = false
        this.dialogLoadingVisible = false
      })
      this.loading = false
      this.dialogLoadingVisible = false
    },
    verifyField(evt) {
      if (this.value_ano && this.value_mes && this.value_empresa) {
        this.disableLoad = false
      }
    },
    getEmpresa(value) {
      if (value) {
        const empresa = this.optionsEmpresa.find(element => element.cod_empresa === value).nombre
        return empresa
      }
    },
    closeModal() {
      this.currentView = null
      console.log('Se cerro vista de parrilla CU!')
    },
    handleClose(done) {
      this.$confirm('¿Realmente deseas cerrar la ventana?')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    onClickChild(value) {
      console.log('onClickChild: ', value) // someValue
      this.dialogFormVisible = value
    }
  }
}
</script>

<style lang="scss">
  .card-header .el-card__header {
    background: #F2F6FC;
  }

  .dialog-loading {
    border-radius: 10px;
    background: white;
  }

  .dialog-loading .el-dialog__header {
    display: none;
  }

  .dialog-loading .el-dialog__header {
		background-color: white;
	}
</style>
