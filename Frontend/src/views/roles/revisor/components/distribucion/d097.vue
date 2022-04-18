<template>
  <div class="components-container">
    <el-row>
      <el-col :span="24" style="border: 0px solid red; text-align: center;">
        <aside>
          <span style="color: black; font-size: 170%;"><b>DIRECCIÓN TÉCNICA DE GESTIÓN DE ENERGÍA</b></span>
        </aside>
      </el-col>
      <el-col :span="24" style="border: 0px solid red; text-align: center;">
        <aside>
          <span style="font-size: 120%;"><b>{{ name }}</b></span>
        </aside>
      </el-col>

      <el-card class="box-card card-header">
        <div slot="header" class="clearfix">
          <span><b>COMPONENTE D | CREG 097</b></span>
        </div>
        <div style="margin-bottom:200px;">
          <el-col :span="24" style="border: 0px solid red; text-align: center;">
            <el-select v-model="value1" clearable placeholder="Año">
              <el-option
                v-for="item in optionsAno"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select><br><br>
            <el-select v-model="value2" clearable placeholder="Mes">
              <el-option
                v-for="item in optionsMes"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select><br><br>
            <el-select v-model="value_empresa" clearable placeholder="Empresa">
              <el-option
                v-for="item in optionsEmpresa"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select><br><br>
            <el-tooltip class="item" effect="dark" content="Nivel de tensión y propiedad del activo del CU a consultar." placement="left" style="margin-left: -1.3em;">
              <i class="el-icon-info" style="color: #304156;" />
            </el-tooltip>
            <el-select v-model="value4" clearable placeholder="NT - PRO">
              <el-option
                v-for="item in optionsNTPRO"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-col>
        </div>
      </el-card>

      <el-col :span="24" style="border: 0px solid red; text-align: right; padding: 10px;">
        <el-button round :loading="false" type="success" icon="el-icon-check" @click="showModal()">Consultar</el-button>
      </el-col>
    </el-row>
    <el-dialog
      :title="modulo"
      :before-close="handleClose"
      :visible.sync="innerVisible"
      fullscreen
      append-to-body
    >
      <component
        :is="currentView"
        @clicked="onClickChild"
      />
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import meses from './options/optionsMes'
import anos from './options/optionsAno'
import empresas from './options/optionsEmpresa'
import Distribucion097 from './modules/distribucion097'

export default {
  name: 'D097',
  components: { Distribucion097 },
  data() {
    return {
      optionsAno: anos,
      optionsMes: meses,
      optionsEmpresa: empresas,
      currentView: null,
      innerVisible: false,
      modulo: null,
      optionsNTPRO: [{
        value: '0',
        label: 'Opción 1'
      }, {
        value: '1',
        label: 'Opción 2'
      }, {
        value: '2',
        label: 'Opción 3'
      }],
      value1: '',
      value2: '',
      value_empresa: '',
      value4: ''
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'roles'
    ])
  },
  created() {

  },
  methods: {
    handleClose(done) {
      this.$confirm('¿Realmente deseas cerrar la ventana?')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    showModal() {
      this.currentView = 'Distribucion097'
      this.innerVisible = true
      this.modulo = this.getTextSelectEmpresa(this.value_empresa) + ' - ' + ' | Módulo Distribución CREG 097'
    },
    getTextSelectEmpresa(val) {
      for (let i = 0; i < this.optionsEmpresa.length; i++) {
        if (this.optionsEmpresa[i].value === val) {
          return this.optionsEmpresa[i].label
        }
      }
      return ''
    },
    onClickChild(value) {
      console.log(value) // someValue
      this.innerVisible = value
    }
  }
}
</script>

<style lang="scss" scoped>
  .placeholder-container div {
    margin: 10px;
  }

  .card-header .el-card__header {
    background: #F2F6FC;
  }
</style>
