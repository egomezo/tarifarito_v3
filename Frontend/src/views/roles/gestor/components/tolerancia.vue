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
          <b>NIVEL DE TOLERANCIA</b>
        </span>
      </div>
      <el-row :gutter="1">
        <el-col :sm="24" :md="8" style="text-align: right;">
          <el-select v-model="value1" placeholder="Año" class="select" @change="verifyVariable($event)">
            <el-option
              v-for="item in optionsAno"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-col>
        <el-col :sm="24" :md="8" style="text-align: center;">
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
        <el-col :sm="24" :md="8" style="text-align: left;">
          <el-input-number
            id="input"
            v-model="variable"
            :disabled="disableVariable"
            :precision="2"
            :step="0.01"
            :min="0"
            :max="10"
            class="input-number"
            @change="verifyVariable('input_variable')"
          />
        </el-col>
      </el-row>
    </el-card>

    <el-card class="box-card margin-card">
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
  getNTolerancia,
  postNTolerancia,
  putNTolerancia
} from '@/api/tarifarito/gestor/nTolerancia'

export default {
  name: 'ViewTolerancia',
  data() {
    return {
      myBackToTopStyle: CONSTANTS.myBackToTopStyle,
      disableLoad: true,
      disableModify: true,
      disableVariable: true,
      disableSelect: true,
      loadingLoad: false,
      loadingModify: false,
      optionsAno: CONSTANTS.optionsAno,
      optionsMes: CONSTANTS.optionsMes,
      value1: '',
      value2: '',
      variable: '',
      date: new Date()
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {},
  methods: {
    async verifyVariable(evt) {
      if (this.value1) {
        this.disableSelect = false
      }
      await getNTolerancia(this.value1).then(response => {
        if (response.length > 0 && this.value2 !== '') {
          const mes = this.optionsMes[this.value2 - 1].key
          if (response[0].meses.hasOwnProperty(mes)) {
            if (evt !== 'input_variable') {
              const length = response[0].meses[mes].length - 1
              const valueVariable = response[0].meses[mes][length].n_tolerancia
              if (valueVariable >= 0) {
                this.variable = valueVariable
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
              this.variable = 0
            }
          }
        } else if (response.length === 0 && this.value2 !== '') {
          if (evt !== 'input_variable') {
            this.disableVariable = false
            this.disableLoad = false
            this.disableModify = true
            this.variable = 0
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
        n_tolerancia: this.variable
      }
      await putNTolerancia(anio, mes, model).then(response => {
        this.disableModify = true
        Message({
          message: 'Registro actualizado con éxito!',
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
      await getNTolerancia(this.value1).then(async response => {
        if (response.length === 0) {
          const model = {
            anio: anio,
            meses: {
              [mes]: [
                {
                  usuario: this.name,
                  fecha_modif: this.date,
                  n_tolerancia: this.variable
                }
              ]
            }
          }
          await postNTolerancia(model).then(response => {
            this.loadingLoad = false
            this.disableLoad = true
            Message({
              message: 'Registro guardado con éxito!',
              type: 'success',
              duration: 2 * 1000
            })
          })
        } else {
          const model = {
            usuario: this.name,
            fecha_modif: this.date,
            n_tolerancia: this.variable
          }
          await putNTolerancia(anio, mes, model).then(response => {
            Message({
              message: 'Registro guardado con éxito!',
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

<style lang="scss">
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

		.cont-select {
			width: 33.3%;
		}

		.select {
			width: 15em;
		}

		.input-number {
			width: 15em;
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
			padding-bottom: 1em;
		}

		.input-number {
			width: 100%;
		}

		.btn {
			width: 100%;
		}
	}
</style>
