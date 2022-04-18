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
          <b>INFORMACIÓN COMERCIAL</b>
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
            filterable
            :disabled="disableSelect"
            placeholder="Empresa"
            class="select-style"
            popper-class="select-popper"
            @change="verifyVariable($event)"
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
    </el-card>

    <el-card class="box-card margin-card">
      <el-row class="cont-row">
        <el-col :sm="24" :md="24">
          <el-row>
            <el-col :sm="24" :md="24">
              <el-tooltip
                class="item"
                effect="dark"
                content="Factor de productividad acumulado."
                placement="top"
              >
                <i class="el-icon-info" style="color: #304156;" />
              </el-tooltip>
              <label>Factor de productividad</label>
            </el-col>
            <el-col :sm="24" :md="24" class="input-padding">
              <el-select
                v-model="value3"
                :disabled="disableVariable"
                class="input-select"
                @change="verifyVariable('input_variable')"
              >
                <el-option
                  v-for="item in optionsFactor"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
              <el-button
                :disabled="disableVariable"
                type="success"
                icon="el-icon-circle-plus-outline"
                class="btn-plain"
                plain
                @click="dialogFormVisible = true"
              />
            </el-col>
          </el-row>
        </el-col>
        <el-col v-for="(item, index) in components" :key="item.id" :sm="24" :md="24">
          <el-row v-if="index !== 0" class="cont-input">
            <el-col :sm="24" :md="24">
              <el-tooltip
                v-if="item.tooltip !== ''"
                class="item"
                effect="dark"
                :content="item.tooltip"
                placement="top"
              >
                <i class="el-icon-info" style="color: #304156;" />
              </el-tooltip>
              <label>{{ item.title }}</label>
            </el-col>
            <el-col :sm="24" :md="24" class="input-padding">
              <el-input-number
                v-model="values[index]"
                :disabled="disableVariable"
                :precision="item.precision"
                :step="item.step"
                :min="item.min"
                :max="item.max"
                :class="item.class"
                @change="verifyVariable('input_variable')"
              />
            </el-col>
          </el-row>
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

    <!-- dialog agregar factor de productividad -->
    <el-dialog title="Agregar" :visible.sync="dialogFormVisible" width="20em" top="10em" custom-class="dialog-class">
      <el-card class="cont-row" style="margin-top: 1.2em;">
        <el-row>
          <el-col :sm="24" :md="24">
            <label>Factor de productividad</label>
          </el-col>
          <el-col :sm="24" :md="24" class="input-padding">
            <el-input-number
              v-model="values[0]"
              :disabled="disableVariable"
              :precision="2"
              :step="0.01"
              :min="0"
              :max="100"
              class="input-number"
              @change="verifyVariable('input_variable')"
            />
          </el-col>
        </el-row>
        <el-divider />
        <el-row>
          <el-col :sm="24" :md="24">
            <el-button type="success" icon="el-icon-check" class="btn" @click="functionConfirmar">Aceptar</el-button>
          </el-col>
        </el-row>
      </el-card>
    </el-dialog>

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
import { Message } from 'element-ui'
import { CONSTANTS } from '../../../../constants/constants'
import componentsIComercial from './../options/info_comercial'
import {
  getIComercialList,
  getIComercial,
  putIComercial,
  postIComercial
} from '@/api/tarifarito/gestor/iComercial'
import {
  getSUIEmpresasList
} from '@/api/tarifarito/sui-empresas'

export default {
  name: 'ViewInfoComercial',
  components: { BackToTop },
  data() {
    // this.getList()
    this.getEmpresasList()
    return {
      components: componentsIComercial,
      disableLoad: true,
      disableModify: true,
      disableVariable: true,
      disableSelect: true,
      loadingLoad: false,
      loadingModify: false,
      dialogFormVisible: false,
      dialogVisible: false,
      loadingFP: false,
      myBackToTopStyle: CONSTANTS.myBackToTopStyle,
      optionsAno: CONSTANTS.optionsAno,
      optionsEmpresa: [],
      optionsFactor: CONSTANTS.optionsFactor,
      value1: '',
      value2: '',
      value3: '',
      inputDialog: '',
      date: new Date(),
      values: [],
      model: {}
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    this.components.forEach((element, index) => {
      this.values[index] = 0
    })
  },
  methods: {
    async getEmpresasList() {
      await getSUIEmpresasList().then((response) => {
        // console.log(response)
        this.optionsEmpresa = JSON.parse(JSON.stringify(response))
      })
    },
    async getList() {
      await getIComercialList().then(response => {
        console.log(response)
      })
    },
    functionConfirmar() {
      const resultFP = this.optionsFactor.find(
        element => element.value === this.values[0]
      )
      console.log('resultFP: ', resultFP)
      if (resultFP === undefined) {
        this.optionsFactor.push({
          value: this.values[0],
          label: this.values[0]
        })
        this.dialogFormVisible = false
        this.value3 = this.values[0]
        this.values[0] = 0
      } else {
        Message({
          message: 'Valor de Factor de productividad ya agregado.',
          type: 'error',
          duration: 2 * 1000
        })
      }
    },
    async verifyVariable(evt) {
      // console.log(evt)
      if (this.value1) {
        this.disableSelect = false
      }
      await getIComercial(this.value1).then(response => {
        if (response.length > 0 && this.value2 !== '') {
          const empresa = `e_${this.value2}`
          console.log('Empresa: ', empresa)
          // console.log('Response: ', response[0].empresas)
          const arrayEmpresas = response[0].empresas
          if (arrayEmpresas.hasOwnProperty(empresa)) {
            if (evt !== 'input_variable') {
              console.log('La tiene: ', arrayEmpresas[empresa])
              const length = arrayEmpresas[empresa].length - 1
              console.log('length: ', length)
              const objValues = arrayEmpresas[empresa][length]
              console.log('element: ', objValues)
              // Verificamos si existen valores de factor de productividad repetidos
              const resultFP = this.optionsFactor.find(
                element => element.value === objValues.factorP
              )
              console.log('Ya tiene el factor: ', resultFP)
              if (resultFP === undefined) {
                this.optionsFactor.push({
                  value: objValues.factorP,
                  label: objValues.factorP
                })
              }
              this.value3 = objValues.factorP
              this.values[1] = objValues.rcnu
              this.values[2] = objValues.ccreg
              this.values[3] = objValues.csspd
              this.values[4] = objValues.rcreg
              this.values[5] = objValues.rsspd
              this.disableVariable = false
              this.disableLoad = true
              this.disableModify = false
            } else {
              this.disableModify = false
            }
          } else {
            if (evt !== 'input_variable') {
              this.disableVariable = false
              this.disableLoad = false
              this.disableModify = true
              this.value3 = ''
              this.values[1] = 0
              this.values[2] = 0
              this.values[3] = 0
              this.values[4] = 0
              this.values[5] = 0
            }
          }
        } else if (response.length === 0 && this.value2 !== '') {
          if (evt !== 'input_variable') {
            this.disableVariable = false
            this.disableLoad = false
            this.disableModify = true
            this.value3 = ''
            this.values[1] = 0
            this.values[2] = 0
            this.values[3] = 0
            this.values[4] = 0
            this.values[5] = 0
          }
        }
      })
    },
    async modifyVariable() {
      this.loadingModify = true
      const anio = this.value1
      const empresa = `e_${this.value2}`
      const model = {
        usuario: this.name,
        fecha_modif: this.date,
        factorP: this.value3,
        rcnu: this.values[1],
        ccreg: this.values[2],
        csspd: this.values[3],
        rcreg: this.values[4],
        rsspd: this.values[5]
      }
      await putIComercial(anio, empresa, model).then(response => {
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
      if (this.value3 !== '') {
        this.loadingLoad = true
        const anio = parseInt(this.value1)
        const empresa = `e_${this.value2}`
        await getIComercial(this.value1).then(async response => {
          if (response.length === 0) {
            const model = {
              anio: anio,
              empresas: {
                [empresa]: [
                  {
                    usuario: this.name,
                    fecha_modif: this.date,
                    factorP: this.value3,
                    rcnu: this.values[1],
                    ccreg: this.values[2],
                    csspd: this.values[3],
                    rcreg: this.values[4],
                    rsspd: this.values[5]
                  }
                ]
              }
            }
            await postIComercial(model).then(response => {
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
              factorP: this.value3,
              rcnu: this.values[1],
              ccreg: this.values[2],
              csspd: this.values[3],
              rcreg: this.values[4],
              rsspd: this.values[5]
            }
            await putIComercial(anio, empresa, model).then(response => {
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
      } else {
        Message({
          message: 'Selecciona un factor de productividad',
          type: 'error',
          duration: 2 * 1000
        })
      }
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

	.input-padding {
		padding-top: 0.5em;
	}

	.dialog-style {
		border: 1px solid red;
	}

  .dialog-class {
    border-radius: 10px;
  }

  .dialog-class .el-dialog__header {
    border-radius: 10px 10px 0px 0px;
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

		.cont-input {
			padding-top: 1.5em;
		}

		.input-select {
			width: 13em;
		}

    .select-style {
      width: 13em;
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

		.cont-input {
			padding-top: 1em;
		}

		.input-select {
			width: 77%;
		}

		.btn-plain {
			width: 21%;
		}

    .select-style {
      width: 100%;
    }

    .select-popper {
      li {
        font-size: 0.45em;
      }
    }
	}
</style>
