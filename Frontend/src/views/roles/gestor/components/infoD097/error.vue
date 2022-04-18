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
          <!-- se utiliza la internacionalizacion -->
          <span><b>{{ $t('error.info') }} D097 | Error</b></span>
        </span>
      </div>
      <el-row class="div-picker">
        <el-col :sm="24" :md="8" style="text-align: right;">
          <el-date-picker
            v-model="task.start_at"
            type="month"
            :placeholder="$t('datePicker.startDate')"
            class="date"
            @change="verifyVariable($event)"
          />
        </el-col>
        <el-col :sm="24" :md="8" style="text-align: center;">
          <el-date-picker
            v-model="task.end_at"
            type="month"
            :disabled="disableEndDate"
            :placeholder="$t('datePicker.endDate')"
            :picker-options="dueDatePickerOptions"
            class="date"
            @change="verifyVariable($event)"
          />
        </el-col>
        <el-col :sm="24" :md="8" style="text-align: left;">
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
      <!-- <el-row :gutter="10">
        <el-col :sm="24" :md="12" class="cont-col-right">
          <el-date-picker
            v-model="end_at"
            type="monthrange"
            :clearable="false"
            :unlink-panels="true"
            align="left"
            range-separator="-"
            :start-placeholder="$t('datePicker.startDate')"
            :end-placeholder="$t('datePicker.endDate')"
            popper-class="select-popper"
            @change="verifyVariable($event)"
          />
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
              :label="item.nombre"
              :value="item.cod_empresa"
            />
          </el-select>
        </el-col>
      </el-row> -->
    </el-card>

    <el-card class="box-card margin-card">
      <el-row class="cont-row">
        <el-col v-for="(item, index) in components" :key="item.id" :sm="24" :md="24">
          <el-row :class="index != 0 ? 'cont-input' : ''">
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
import moment from 'moment'
import { mapGetters } from 'vuex'
import BackToTop from '@/components/BackToTop'
import { Message } from 'element-ui'
import { CONSTANTS } from '../../../../../constants/constants'
import d097_resolucion from './../../options/d097_error'
import {
  getD097ErrorList,
  getD097Error,
  putD097Error,
  postD097Error
} from '@/api/tarifarito/gestor/D097_error'
import { getSUIEmpresasList } from '@/api/tarifarito/sui-empresas'

export default {
  name: 'ViewD097Error',
  components: { BackToTop },
  data() {
    this.getList()
    this.getEmpresasList()
    return {
      components: d097_resolucion,
      disableLoad: true,
      disableModify: true,
      disableVariable: true,
      disableEndDate: true,
      disableSelect: true,
      loadingLoad: false,
      loadingModify: false,
      myBackToTopStyle: CONSTANTS.myBackToTopStyle,
      optionsAno: CONSTANTS.optionsAno,
      optionsEmpresa: [],
      value2: '',
      date: new Date(),
      values: [],
      model: {},
      task: {
        start_at: '',
        end_at: ''
      },
      dueDatePickerOptions: {
        disabledDate: this.disabledDueDate
      }
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
    disabledDueDate(time) {
      return time.getTime() < this.task.start_at
    },
    async getEmpresasList() {
      await getSUIEmpresasList().then(response => {
        // console.log(response)
        this.optionsEmpresa = JSON.parse(JSON.stringify(response))
      })
    },
    async getList() {
      await getD097ErrorList().then(response => {
        console.log(response)
      })
    },
    async verifyVariable(evt) {
      console.log(evt)
      if (this.task.start_at) {
        this.disableEndDate = false
      } else {
        this.disableEndDate = true
      }
      if (this.task.start_at && this.task.end_at) {
        this.disableSelect = false
        this.queryVariable(evt)
      } else {
        this.disableSelect = true
        this.disableVariable = true
        this.disableLoad = true
        this.disableModify = true
      }
    },
    async queryVariable(evt) {
      const f_inicial = moment(this.task.start_at).utc().format('YYYY-MM')
      const f_final = moment(this.task.end_at).utc().format('YYYY-MM')
      await getD097Error(f_inicial, f_final).then(response => {
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
              this.values[0] = objValues.cdi
              this.values[1] = objValues.cdm
              this.values[2] = objValues.cd2
              this.values[3] = objValues.cd3
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
              this.values[0] = 0
              this.values[1] = 0
              this.values[2] = 0
              this.values[3] = 0
            }
          }
        } else if (response.length === 0 && this.value2 !== '') {
          if (evt !== 'input_variable') {
            this.disableVariable = false
            this.disableLoad = false
            this.disableModify = true
            this.values[0] = 0
            this.values[1] = 0
            this.values[2] = 0
            this.values[3] = 0
          }
        }
      })
    },
    async modifyVariable() {
      this.loadingModify = true
      const f_inicial = moment(this.task.start_at).utc().format('YYYY-MM')
      const f_final = moment(this.task.end_at).utc().format('YYYY-MM')
      const empresa = `e_${this.value2}`
      const model = {
        usuario: this.name,
        fecha_modif: this.date,
        cdi: this.values[0],
        cdm: this.values[1],
        cd2: this.values[2],
        cd3: this.values[3]
      }
      await putD097Error(f_inicial, f_final, empresa, model).then(response => {
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
      const f_inicial = moment(this.task.start_at).utc().format('YYYY-MM')
      const f_final = moment(this.task.end_at).utc().format('YYYY-MM')
      const empresa = `e_${this.value2}`
      await getD097Error(f_inicial, f_final).then(async response => {
        if (response.length === 0) {
          const model = {
            f_inicial: f_inicial,
            f_final: f_final,
            empresas: {
              [empresa]: [
                {
                  usuario: this.name,
                  fecha_modif: this.date,
                  cdi: this.values[0],
                  cdm: this.values[1],
                  cd2: this.values[2],
                  cd3: this.values[3]
                }
              ]
            }
          }
          await postD097Error(model).then(response => {
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
            cdi: this.values[0],
            cdm: this.values[1],
            cd2: this.values[2],
            cd3: this.values[3]
          }
          await putD097Error(f_inicial, f_final, empresa, model).then(response => {
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

    .div-picker .date {
      width: 15em;
    }

		.picker-popper {
			.el-date-picker__header{
				// custom header style here
				background: chocolate;
			}
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

    .div-picker .date {
      width: 100%;
      padding-bottom: 1em;
    }

		.select-popper {
			li {
				font-size: 0.45em;
			}
		}
	}
</style>
