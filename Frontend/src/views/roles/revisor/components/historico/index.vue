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
    </el-row>

    <el-card class="box-card card-header">
      <div slot="header" class="clearfix">
        <span class="text-page">
          <b>Histórico / Consultas / Costo unitario</b>
        </span>
      </div>

      <el-row class="cont-row" style="text-align: center;">
        <el-col :sm="24" :md="24">
          <el-select v-model="value_ano" placeholder="Año" class="select-style" @change="verifyField($event, '')">
            <el-option
              v-for="item in optionsAno"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-col>
        <el-col :sm="24" :md="24" style="padding-top: 1em;">
          <el-select v-model="value_mes" placeholder="Mes" class="select-style" @change="verifyField($event, '')">
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
            :loading-text="loadingTextEmpresa"
            @change="verifyField($event, 'get_mercados')"
          >
            <el-option
              v-for="item in optionsEmpresa"
              :key="item.cod_empresa"
              :label="`${item.cod_empresa} - ${item.nombre}`"
              :value="item.cod_empresa"
            />
          </el-select>
        </el-col>
        <el-col :sm="24" :md="24" style="padding-top: 1em;">
          <el-select
            v-model="value_mercado"
            filterable
            placeholder="Mercado"
            class="select-style"
            :loading="loadingMercados"
            :loading-text="loadingTextMercado"
            :disabled="disabledMercados"
            @change="verifyField($event, '')"
          >
            <el-option
              v-for="item in optionsMercados"
              :key="item.cod_mercado"
              :label="`${item.cod_mercado} - ${item.nom_mercado}`"
              :value="item.cod_mercado"
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
            @click.native.prevent="setDataComponentes"
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
      <component :is="currentView" :msgviewparent="dataHistorico" @clicked="onClickChild" />
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import gridHistorico from './grid-historico'
import { CONSTANTS } from '../../../../../constants/constants'
import { getSUIEmpresasList } from '@/api/tarifarito/sui-empresas'
import { getSUIMercados } from '@/api/tarifarito/sui-empresa-mercado'

export default {
  name: 'ViewHistorico',
  components: {
    gridHistorico
  },
  data() {
    return {
      disableLoad: true,
      dataHistorico: {},
      currentView: null,
      loading: false,
      dialogFormVisible: false,
      optionsAno: CONSTANTS.optionsAno,
      optionsMes: CONSTANTS.optionsMes,
      loadingEmp: true,
      loadingMercados: true,
      disabledMercados: true,
      loadingTextEmpresa: 'Cargando empresas...',
      optionsEmpresa: [],
      optionsMercados: [],
      value_ano: '',
      value_mes: '',
      value_empresa: '',
      value_mercado: '',
      loadingTextMercado: 'Cargando mercados...',
      title_modulo: ''
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    this.getEmpresasList()
  },
  methods: {
    async getEmpresasList() {
      await getSUIEmpresasList().then(result => {
        this.loadingEmp = false
        this.optionsEmpresa = JSON.parse(JSON.stringify(result))
        // CONDICIONES INICIALES - PRUEBA
        this.value_ano = 2020
        this.value_mes = 4
        this.verifyField()
      })
      // eslint-disable-next-line handle-callback-err
        .catch(err => {
          this.loadingTextEmpresa = 'Error, recargue la página'
          this.getEmpresasList()
        })
    },
    async getMercados(empresa) {
      await getSUIMercados(empresa).then(result => {
        this.loadingMercados = false
        // console.log('MERCADOS -> ', result)
        this.optionsMercados = JSON.parse(JSON.stringify(result[0].mercados))
        this.verifyField()
        this.disabledMercados = false
        this.value_mercado = 'Seleccione un mercado'
      })
      // eslint-disable-next-line handle-callback-err
        .catch(err => {
          this.loadingTextMercado = 'Error, recargue la página'
        })
    },
    async setDataComponentes() {
      this.loading = true
      this.dataHistorico.ano = this.value_ano
      this.dataHistorico.mes = this.value_mes
      this.dataHistorico.cod_empresa = this.value_empresa
      this.dataHistorico.cod_mercado = this.value_mercado
      this.dataHistorico.empresa = this.getEmpresa(this.value_empresa)
      this.dataHistorico.mercado = this.getMercado(this.value_mercado)
      this.dialogFormVisible = true
      this.currentView = 'gridHistorico'
      this.loading = false
    },
    verifyField(empresa, option) {
      if (option === 'get_mercados') {
        this.disabledMercados = true
        this.value_mercado = 'Cargando mercados...'
        this.optionsMercados = []
        this.getMercados(empresa)
        this.disableLoad = true
      }
      if (this.value_ano && this.value_mes && this.value_empresa && this.value_mercado !== 'Cargando mercados...') {
        this.disableLoad = false
        this.title_modulo = 'Histórico | Consultas CU | ' + this.getEmpresa(this.value_empresa)
      }
    },
    getEmpresa(value) {
      if (value) {
        const empresa = this.optionsEmpresa.find(element => element.cod_empresa === value).nombre
        return empresa
      }
    },
    getMercado(value) {
      if (value) {
        const mercado = this.optionsMercados.find(element => element.cod_mercado === value).nom_mercado
        return mercado
      }
    },
    closeModal() {
      this.currentView = null
      console.log('Se cerro vista tabla de componentes!')
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
</style>
