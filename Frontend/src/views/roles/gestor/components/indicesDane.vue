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
          <b>ÍNDICES DANE</b>
        </span>
      </div>
      <el-row :gutter="10">
        <el-col :sm="24" :md="12" class="cont-col-right">
          <el-select v-model="value1" placeholder="Año" class="select" @change="verifyVariable($event)">
            <el-option
              v-for="item in optionsAno"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-col>
        <el-col :sm="24" :md="12">
          <el-select
            v-model="value2"
            :disabled="disableSelect"
            placeholder="Mes"
            class="select"
            @change="verifyVariable($event)"
          >
            <el-option
              v-for="item in optionsMes"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-col>
      </el-row>
    </el-card>

    <el-card class="box-card margin-card">
      <el-row class="cont-row">
        <el-col :sm="24" :md="24">
          <label for="input1">IPC</label>
          <el-input-number
            id="input1"
            v-model="input1"
            :disabled="disableVariable"
            :precision="2"
            :step="0.01"
            :min="0"
            :max="200"
            class="input-number"
            @change="verifyVariable('input_variable')"
          />
        </el-col>
        <el-col :sm="24" :md="24" style="padding-top: 1em;">
          <label for="input2">IPP</label>
          <el-input-number
            id="input2"
            v-model="input2"
            :disabled="disableVariable"
            :precision="2"
            :step="0.01"
            :min="0"
            :max="200"
            class="input-number"
            @change="verifyVariable('input_variable')"
          />
        </el-col>
      </el-row>

      <el-divider />

      <el-row :gutter="10">
        <el-col :sm="24" :md="12" class="cont-col-right">
          <el-button
            :disabled="disableModify"
            type="primary"
            icon="el-icon-refresh"
            :loading="loadingModify"
            class="btn"
            @click.native.prevent="modifyVariable"
          >Modificar</el-button>
        </el-col>
        <el-col :sm="24" :md="12">
          <el-button
            :disabled="disableLoad"
            type="success"
            icon="el-icon-check"
            :loading="loadingLoad"
            class="btn"
            @click.native.prevent="saveVariable"
          >Cargar</el-button>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { Message } from 'element-ui'
import { CONSTANTS } from '../../../../constants/constants'
import {
  getIDaneList,
  getIDane,
  putIDane,
  postIDane
} from '@/api/tarifarito/gestor/iDane'

export default {
  name: 'ViewIndicesDane',
  data() {
    // this.getList()
    return {
      disableLoad: true,
      disableModify: true,
      disableVariable: true,
      disableSelect: true,
      loadingLoad: false,
      loadingModify: false,
      myBackToTopStyle: CONSTANTS.myBackToTopStyle,
      optionsAno: CONSTANTS.optionsAnoDane,
      optionsMes: CONSTANTS.optionsMes,
      value1: '',
      value2: '',
      input1: 0,
      input2: 0,
      date: new Date()
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {},
  methods: {
    async getList() {
      await getIDaneList().then(response => {
        console.log(response)
      })
    },
    async verifyVariable(evt) {
      // console.log(evt)
      if (this.value1) {
        this.disableSelect = false
      }
      await getIDane(this.value1).then(response => {
        if (response.length > 0 && this.value2 !== '') {
          const mes = this.optionsMes[this.value2 - 1].key
          if (response[0].meses.hasOwnProperty(mes)) {
            if (evt !== 'input_variable') {
              console.log(response)
              const length = response[0].meses[mes].length - 1
              const valueVariableIPC = response[0].meses[mes][length].ipc
              const valueVariableIPP = response[0].meses[mes][length].ipp
              if (valueVariableIPC >= 0 || valueVariableIPP >= 0) {
                this.input1 = valueVariableIPC
                this.input2 = valueVariableIPP
                this.disableVariable = false
                this.disableLoad = true
                this.disableModify = false
              }
            } else {
              this.disableModify = false
            }
          } else {
            if (evt !== 'input_variable') {
              this.disableVariable = false
              this.disableLoad = false
              this.disableModify = true
              this.input1 = 0
              this.input2 = 0
            }
          }
        } else if (response.length === 0 && this.value2 !== '') {
          if (evt !== 'input_variable') {
            this.disableVariable = false
            this.disableLoad = false
            this.disableModify = true
            this.input1 = 0
            this.input2 = 0
          }
        }
      })
    },
    async modifyVariable() {
      this.loadingModify = true
      const anio = this.value1
      const mes = this.optionsMes[this.value2 - 1].key
      const model = {
        usuario: this.name,
        fecha_modif: this.date,
        ipc: this.input1,
        ipp: this.input2
      }
      await putIDane(anio, mes, model).then(response => {
        this.disableModify = true
        Message({
          message: 'Registros actualizados con éxito!',
          type: 'success',
          duration: 2 * 1000
        })
        this.loadingModify = false
      })
    },
    async saveVariable() {
      this.loadingLoad = true
      const anio = parseInt(this.value1)
      const mes = this.optionsMes[this.value2 - 1].key
      await getIDane(this.value1).then(async response => {
        if (response.length === 0) {
          const model = {
            anio: anio,
            meses: {
              [mes]: [
                {
                  usuario: this.name,
                  fecha_modif: this.date,
                  ipc: this.input1,
                  ipp: this.input2
                }
              ]
            }
          }
          await postIDane(model).then(response => {
            this.loadingLoad = false
            this.disableLoad = true
            Message({
              message: 'Registros guardados con éxito!',
              type: 'success',
              duration: 2 * 1000
            })
          })
        } else {
          const model = {
            usuario: this.name,
            fecha_modif: this.date,
            ipc: this.input1,
            ipp: this.input2
          }
          await putIDane(anio, mes, model).then(response => {
            Message({
              message: 'Registros guardados con éxito!',
              type: 'success',
              duration: 2 * 1000
            })
          })
          this.loadingLoad = false
          this.disableLoad = true
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
	.text-header {
		color: black;
	}

	.margin-card {
		margin-top: 1em;
	}

	.cont-row {
		text-align: center;
  }

  .card-header .el-card__header {
    background: #F2F6FC;
  }

	// Pantallas superiores a 800px (PC)
	@media screen and (min-width: 800px) {
    .div-cont {
      padding-top: 1.5em;
      padding-left: 3em;
      padding-right: 3em;
    }

		.text-header {
			font-size: x-large;
		}

		.text-user {
			font-size: large;
		}

		.text-page {
			font-size: medium;
		}

		.cont-col-right {
			text-align: right;
		}

		.select {
			width: 13em;
		}

		.input-number {
			width: 17em;
		}

		.btn {
			width: 10em;
		}
	}

	// Pantallas inferiores a 800px (mobile)
	@media screen and (max-width: 800px) {
    .div-cont {
      padding: 1em;
    }

		.text-header {
			font-size: small;
		}

		.text-user {
			font-size: small;
		}

		.text-page {
			font-size: small;
		}

		.cont-col-right {
			padding-bottom: 0.5em;
		}

		.select {
			width: 100%;
		}

		.input-number {
			width: 100%;
		}

		.btn {
			width: 100%;
		}
	}
</style>
