<template>
  <div v-loading="loading">
    <el-card class="box-card card-cpte" style="height: 72vh; overflow-y:scroll;">
      <el-card class="box-card card-cpte-1" :class="valoresDiferencia ? 'enlarge' : 'shrink'">
        <el-card
          v-if="!loading"
          style="padding-left: 2em; padding-right: 2em; margin-bottom: 1em; border: 0px solid red; width: 100%;"
        >
          <el-row style="font-weight: bold; padding-bottom: 1%; text-align: center;">
            <el-col style="border: 0px solid red; text-align: left;" :span="13">
              <span>CONCEPTO</span>
              <span style="color: white;">{{ actualiza }}</span>
              <!-- No borrar el span, este componente permite renderizar la diferencia de valores -->
            </el-col>
            <el-col style="border: 0px solid red;" :span="2">
              <span>UNIDAD</span>
            </el-col>
            <el-col style="border: 0px solid red;" :span="valoresDiferencia ? 3 : 9">
              <span>TARIFARITO</span>
            </el-col>
            <el-col v-if="valoresDiferencia" :span="valoresDiferencia ? 3 : 0">
              <span>REVISIÓN</span>
            </el-col>
            <el-col v-if="valoresDiferencia" :span="valoresDiferencia ? 3 : 0">
              <span>DIFERENCIA</span>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="24">
              <el-collapse accordion>
                <el-collapse-item v-for="item in components" :key="item.title" :name="item.name">
                  <template slot="title">
                    {{ item.title }}
                    <i class="header-icon el-icon-information" />
                  </template>
                  <el-row v-for="value in item.data" :key="value.campo">
                    <el-col
                      :span="valoresDiferencia ? 13 : 11"
                      style="padding-left: 2%; border: 0px solid blue;"
                    >
                      <span>{{ value.concepto }}</span>
                    </el-col>
                    <el-col
                      style="border: 0px solid blue; text-align: center;"
                      :span="valoresDiferencia ? 2 : 6"
                    >
                      <span>{{ value.unidad }}</span>
                    </el-col>
                    <span v-for="valorInput in value.inputs" :key="valorInput.key">
                      <span v-if="valorInput.start === true && valorInput.diferencia === false">
                        <el-col
                          v-if="valorInputDefault === valorInput.show"
                          style="border: 0px solid yellow; text-align: center;"
                          :span="valoresDiferencia ? 3 : 6"
                        >
                          <input
                            v-if="values[valorInput.key]"
                            v-model="values[valorInput.key].values"
                            :type="valorInput.type"
                            :placeholder="valorInput.placeholder"
                            style="width: 95%; height: 2em; margin-bottom: 0.5em;"
                            :disabled="true"
                          >
                        </el-col>
                      </span>
                      <span v-else-if="valorInput.start === false && valorInput.diferencia === false">
                        <el-col
                          v-if="valoresDiferencia === valorInput.show"
                          style="border: 0px solid red;"
                          :span="valoresDiferencia ? 3 : 1"
                        >
                          <input
                            v-if="values[valorInput.key]"
                            v-model="values[valorInput.key].values"
                            :type="valorInput.type"
                            :placeholder="valorInput.placeholder"
                            :disabled="valorInput.disabled"
                            style="width: 95%; height: 2em; margin-bottom: 0.5em;"
                            :style="{'display': valoresDiferencia ? 'block' : 'none'}"
                            @input="formula()"
                          >
                        </el-col>
                      </span>
                      <span v-else>
                        <el-col
                          v-if="valoresDiferencia === valorInput.show"
                          style="border: 0px solid red;"
                          :span="valoresDiferencia ? 3 : 0"
                        >
                          <input
                            v-model="values[valorInput.key].values"
                            :type="valorInput.type"
                            :placeholder="valorInput.placeholder"
                            :disabled="true"
                            style="width: 95%; height: 2em; margin-bottom: 0.5em;"
                            :style="{'display': valoresDiferencia ? 'block' : 'none'}"
                          >
                        </el-col>
                      </span>
                    </span>
                  </el-row>
                </el-collapse-item>
              </el-collapse>
            </el-col>
          </el-row>
        </el-card>
      </el-card>
    </el-card>

    <div class="footer">
      <el-row style="padding-left: 2.5em;">
        <el-col :span="8" style="border: 0px solid yellow;">
          <span>
            <b>Cpte. TARIFARITO {{ ntprop }} $/kWh</b>
          </span>
          <el-input v-model="cpteCalculado" type="number" style="width: 39%;" readonly />
        </el-col>
        <el-col :span="8" style="border: 0px solid yellow;">
          <span>
            <b>Cpte. publicado {{ ntprop }} $/kWh</b>
          </span>
          <el-input v-model="cptePublicado" type="number" style="width: 39%;" readonly />
        </el-col>
        <el-col :span="8" style="border: 0px solid yellow;">
          <span>
            <b>Cpte. calculado revisión {{ ntprop }} $/kWh</b>
          </span>
          <el-input v-model="valuePruebas" type="text" style="width: 39%;" readonly />
        </el-col>
      </el-row>
      <el-row style="padding-left: 2.5em;">
        <el-col :span="24" style="border: 0px solid yellow;">
          <span>Fórmula componente</span>
          <el-tooltip class="item" effect="dark" content="Fórmula" placement="top-start">
            <i class="el-icon-info" style="color: #304156;" />
          </el-tooltip>
        </el-col>
      </el-row>

      <el-row :gutter="10" style="padding-right: 0em;">
        <el-col :sm="24" :md="21" class="cont-btn" style="text-align: right;">
          <el-button
            type="primary"
            class="btnVerify"
            @click="valoresDiferencia = !valoresDiferencia"
          >Calcular</el-button>
        </el-col>
        <el-col :sm="24" :md="3">
          <el-button v-if="!valoresDiferencia" class="btn" type="success" @click="verificar">Verificado</el-button>
          <el-button v-if="valoresDiferencia" class="btn" type="danger" @click="reportar">Reportar</el-button>
        </el-col>
      </el-row>
    </div>

    <!-- dialog mensaje revisión del componente -->
    <el-dialog
      title="Tarifarito reporta"
      :visible.sync="dialogFormVisible"
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
import moment from 'moment'
import { mapGetters } from 'vuex'
import { Message } from 'element-ui'
import logTarifarito from '../../../../../../assets/logo_buho.png'
import componentePerdidas from './../options/componentP'
import { getCptePValues, postMDBCpteP } from '@/api/tarifarito/revisor/componentP'

export default {
  name: 'ViewG',
  props: {
    messagecomponent: {
      type: Object,
      default: function() {
        return { message: null }
      }
    }
  },
  data() {
    return {
      logo: logTarifarito,
      valorInputDefault: true,
      valoresDiferencia: false,
      components: componentePerdidas,
      dataParentP: null,
      ntprop: '',
      input: 0,
      input1: 0,
      cptePublicado: 0,
      cpteCalculado: 0,
      valuePruebas: 0,
      values: [],
      actualiza: false,
      dataCpteG: [],
      keysValues: [],
      loading: true,
      dialogFormVisible: false,
      novedad: null,
      modelMDBCpteG: {},
      modelValues: {
        campo16: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
      }
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    this.initData()
  },
  methods: {
    async initData() {
      // Data enviada del padre
      this.dataParentP = JSON.parse(JSON.stringify(this.messagecomponent))
      // Se traen valores de variables
      console.log('dataParentP --> ', this.dataParentP)
      this.cptePublicado = parseFloat(
        this.dataParentP.componentes[0].component_p[0].cpte_publicado
      ).toFixed(3)
      this.cpteCalculado = parseFloat(
        this.dataParentP.componentes[0].component_p[0].cpte_calculado
      ).toFixed(3)
      this.ntprop = this.dataParentP.nt_prop
      if (this.ntprop[0] === '1') {
        this.ntprop = 'NT1'
      }
      if (this.ntprop[0] === '2') {
        this.ntprop = 'NT2'
      }
      if (this.ntprop[0] === '3') {
        this.ntprop = 'NT3'
      }
      if (this.ntprop[0] === '4') {
        this.ntprop = 'NT4'
      }
      this.cpte = this.dataParentP.componentes[0].component_p[0].value
      if (this.dataParentP.hasOwnProperty('estado')) {
        this.modelValues = this.dataParentP.values
        // console.log('respons: ', this.modelValues)
        this.initInputs()
        this.loading = false
      } else {
        await getCptePValues(this.dataParentP, this.cpte).then(response => {
          this.modelValues = JSON.parse(JSON.stringify(response[0].values))
          // console.log('respons: ', this.modelValues)
          this.initInputs()
          this.loading = false
        })
      }
    },
    initInputs() {
      let valores = []
      let diferencia = 0
      this.keysValues = Object.keys(this.modelValues)
      // console.log('LLAVE: ', this.keysValues)
      this.components.forEach((item, index) => {
        item.data.forEach((input, idx) => {
          input.inputs.forEach(campo => {
            if (campo.diferencia === false) {
              // console.log('CAMPO -> ', campo)
              // si se quiere mayor precision colocar .toFixed(12) identificando cuales numeros tienen decimales largos
              const valor = this.modelValues[this.keysValues[index]][idx]
              valores.push(valor)
              this.values[campo.key] = {
                placeholder: campo.placeholder,
                show: campo.show,
                values: valor
              }
            } else {
              diferencia = valores[0] - valores[1]
              this.values[campo.key] = {
                placeholder: campo.placeholder,
                show: campo.show,
                values: diferencia
              }
              valores = []
            }
          })
        })
      })
      this.formula()
      // console.log('VALUES ->> ', this.values)
    },
    diferenciaFormula() {
      let valores = []
      let diferencia = 0

      this.components.forEach((item, index) => {
        item.data.forEach((input, idx) => {
          input.inputs.forEach(campo => {
            if (campo.diferencia === false) {
              // console.log('CAMPO -> ', campo)
              valores.push(
                parseFloat(this.values[campo.key].values).toPrecision(12)
              )
            } else {
              // console.log(`${campo.key}`, valores[0], `${campo.key}`, valores[1], ' = ', valores[0] - valores[1])
              diferencia = valores[0] - valores[1]
              this.values[campo.key].values = diferencia
              valores = []
            }
          })
        })
      })
      // console.log('MODEL --> ', this.values)
    },
    verificar() {
      this.valoresDiferencia = false
      this.$emit('clicked', false)
    },
    formula() {
      this.valuePruebas = 0
      // console.log('VALUES -> ', this.values)
      let campo8 = 0
      let campo9 = 0
      let campo16 = 0
      let campo20 = 0
      let campo17 = 0
      let campo21 = 0
      let campo18 = 0
      let campo22 = 0
      let campo19 = 0
      let campo23 = 0
      let campo24 = 0
      let campo25 = 0
      let campo26 = 0
      let campo27 = 0

      if (this.cpte === 'P015') {
        campo8 = parseFloat(this.values['c2_2'].values) + parseFloat(this.values['c3_2'].values) + parseFloat(this.values['c4_2'].values) + parseFloat(this.values['c5_2'].values) + parseFloat(this.values['c6_2'].values) + parseFloat(this.values['c7_2'].values)

        campo9 = (parseFloat(this.values['c3_2'].values) + parseFloat(this.values['c5_2'].values) + parseFloat(this.values['c7_2'].values)) / parseFloat(this.values['c8_2'].values)

        campo16 = (parseFloat(this.values['c1_2'].values) * (parseFloat(this.values['c10_2'].values) / 100 + parseFloat(this.values['c9_2'].values))) / (1 - (parseFloat(this.values['c10_2'].values) / 100 + parseFloat(this.values['c9_2'].values)))

        campo20 = (parseFloat(this.values['c14_2'].values) * parseFloat(this.values['c10_2'].values) / 100) / (1 - parseFloat(this.values['c10_2'].values) / 100)

        campo17 = (parseFloat(this.values['c1_2'].values) * (parseFloat(this.values['c11_2'].values) / 100 + parseFloat(this.values['c9_2'].values))) / (1 - (parseFloat(this.values['c11_2'].values) / 100 + parseFloat(this.values['c9_2'].values)))

        campo21 = (parseFloat(this.values['c14_2'].values) * parseFloat(this.values['c11_2'].values) / 100) / (1 - parseFloat(this.values['c11_2'].values) / 100)

        campo18 = (parseFloat(this.values['c1_2'].values) * (parseFloat(this.values['c12_2'].values) / 100 + parseFloat(this.values['c9_2'].values))) / (1 - (parseFloat(this.values['c12_2'].values) / 100 + parseFloat(this.values['c9_2'].values)))

        campo22 = (parseFloat(this.values['c14_2'].values) * parseFloat(this.values['c12_2'].values) / 100) / (1 - parseFloat(this.values['c12_2'].values) / 100)

        campo19 = (parseFloat(this.values['c1_2'].values) * (parseFloat(this.values['c13_2'].values) / 100 + parseFloat(this.values['c9_2'].values))) / (1 - (parseFloat(this.values['c13_2'].values) / 100 + parseFloat(this.values['c9_2'].values)))

        campo23 = (parseFloat(this.values['c14_2'].values) * parseFloat(this.values['c13_2'].values) / 100) / (1 - parseFloat(this.values['c13_2'].values) / 100)

        campo24 = parseFloat(this.values['c16_2'].values) + parseFloat(this.values['c20_2'].values) + parseFloat(this.values['c15_2'].values)

        campo25 = parseFloat(this.values['c17_2'].values) + parseFloat(this.values['c21_2'].values) + parseFloat(this.values['c15_2'].values)

        campo26 = parseFloat(this.values['c18_2'].values) + parseFloat(this.values['c22_2'].values) + parseFloat(this.values['c15_2'].values)

        campo27 = parseFloat(this.values['c19_2'].values) + parseFloat(this.values['c23_2'].values) + parseFloat(this.values['c15_2'].values)
      } else if (this.cpte === 'P097') {
        campo8 = parseFloat(this.values['c2_2'].values) + parseFloat(this.values['c3_2'].values) + parseFloat(this.values['c4_2'].values) + parseFloat(this.values['c5_2'].values) + parseFloat(this.values['c6_2'].values) + parseFloat(this.values['c7_2'].values)

        campo9 = (parseFloat(this.values['c3_2'].values) + parseFloat(this.values['c5_2'].values) + parseFloat(this.values['c7_2'].values)) / parseFloat(this.values['c8_2'].values)

        campo16 = (parseFloat(this.values['c1_2'].values) * (parseFloat(this.values['c10_2'].values) / 100 + parseFloat(this.values['c9_2'].values))) / (1 - (parseFloat(this.values['c10_2'].values) / 100 + parseFloat(this.values['c9_2'].values)))

        campo20 = (parseFloat(this.values['c14_2'].values) * parseFloat(this.values['c10_2'].values) / 100) / (1 - parseFloat(this.values['c10_2'].values) / 100) + parseFloat(this.values['c15_2'].values)

        campo17 = (parseFloat(this.values['c1_2'].values) * (parseFloat(this.values['c11_2'].values) / 100 + parseFloat(this.values['c9_2'].values))) / (1 - (parseFloat(this.values['c11_2'].values) / 100 + parseFloat(this.values['c9_2'].values)))

        campo21 = (parseFloat(this.values['c14_2'].values) * parseFloat(this.values['c11_2'].values) / 100) / (1 - parseFloat(this.values['c11_2'].values) / 100) + parseFloat(this.values['c15_2'].values)

        campo18 = (parseFloat(this.values['c1_2'].values) * (parseFloat(this.values['c12_2'].values) / 100 + parseFloat(this.values['c9_2'].values))) / (1 - (parseFloat(this.values['c12_2'].values) / 100 + parseFloat(this.values['c9_2'].values)))

        campo22 = (parseFloat(this.values['c14_2'].values) * parseFloat(this.values['c12_2'].values) / 100) / (1 - parseFloat(this.values['c12_2'].values) / 100) + parseFloat(this.values['c15_2'].values)

        campo19 = (parseFloat(this.values['c1_2'].values) * (parseFloat(this.values['c13_2'].values) / 100 + parseFloat(this.values['c9_2'].values))) / (1 - (parseFloat(this.values['c13_2'].values) / 100 + parseFloat(this.values['c9_2'].values)))

        campo23 = (parseFloat(this.values['c14_2'].values) * parseFloat(this.values['c13_2'].values) / 100) / (1 - parseFloat(this.values['c13_2'].values) / 100) + parseFloat(this.values['c15_2'].values)

        campo24 = parseFloat(this.values['c16_2'].values) + parseFloat(this.values['c20_2'].values)

        campo25 = parseFloat(this.values['c17_2'].values) + parseFloat(this.values['c21_2'].values)

        campo26 = parseFloat(this.values['c18_2'].values) + parseFloat(this.values['c22_2'].values)

        campo27 = parseFloat(this.values['c19_2'].values) + parseFloat(this.values['c23_2'].values)
      }

      this.values['c8_2'].values = campo8
      this.values['c9_2'].values = campo9
      this.values['c16_2'].values = campo16
      this.values['c20_2'].values = campo20
      this.values['c17_2'].values = campo17
      this.values['c21_2'].values = campo21
      this.values['c18_2'].values = campo18
      this.values['c22_2'].values = campo22
      this.values['c19_2'].values = campo19
      this.values['c23_2'].values = campo23
      this.values['c24_2'].values = campo24
      this.values['c25_2'].values = campo25
      this.values['c26_2'].values = campo26
      this.values['c27_2'].values = campo27

      if (this.ntprop === 'NT1') {
        this.valuePruebas = campo24.toFixed(3)
      }
      if (this.ntprop === 'NT2') {
        this.valuePruebas = campo25.toFixed(3)
      }
      if (this.ntprop === 'NT3') {
        this.valuePruebas = campo26.toFixed(3)
      }
      if (this.ntprop === 'NT4') {
        this.valuePruebas = campo27.toFixed(3)
      }

      console.log('MODEL antes diferencia --> ', this.values)
      this.diferenciaFormula()
      console.log('MODEL despues diferencia --> ', this.values)
    },
    reportar() {
      this.dialogFormVisible = true
    },
    async registrarNovedad() {
      if (this.novedad) {
        this.modelMDBCpteG = {
          usuario: this.name,
          ano: Number(this.dataParentP.ano),
          mes: Number(this.dataParentP.mes),
          cod_empresa: Number(this.dataParentP.id_empresa),
          nom_empresa: this.dataParentP.nombre_empresa,
          cod_mercado: Number(this.dataParentP.id_mercado),
          nom_mercado: this.dataParentP.mercado,
          componente: this.cpte.toUpperCase(),
          nt_prop: this.dataParentP.nt_prop,
          novedad: this.novedad,
          fecha_modif: moment(new Date()).format('DD/MM/YYYY HH:mm:ss'),
          estado: 'En gestión',
          componentes: [{ 'component_p': [{ 'value': this.cpte, 'cpte_publicado': Number(this.cptePublicado), 'cpte_calculado': Number(this.valuePruebas) }] }],
          values: {
            'CPTEG': [
              this.values['c1_2'].values
            ],
            'CPTET': [
              this.values['c14_2'].values
            ],
            'IPRSTN': [
              this.values['c9_2'].values
            ],
            'DEMANDACOMERCIAL': [
              this.values['c8_2'].values,
              this.values['c2_2'].values,
              this.values['c3_2'].values,
              this.values['c4_2'].values,
              this.values['c5_2'].values,
              this.values['c6_2'].values,
              this.values['c7_2'].values
            ],
            'PERDIDASG_NT1': [
              this.values['c16_2'].values
            ],
            'PERDIDAST_NT1': [
              this.values['c20_2'].values,
              this.values['c10_2'].values
            ],
            'PERDIDASG_NT2': [
              this.values['c17_2'].values
            ],
            'PERDIDAST_NT2': [
              this.values['c21_2'].values,
              this.values['c11_2'].values
            ],
            'PERDIDASG_NT3': [
              this.values['c18_2'].values
            ],
            'PERDIDAST_NT3': [
              this.values['c22_2'].values,
              this.values['c12_2'].values
            ],
            'PERDIDASG_NT4': [
              this.values['c19_2'].values
            ],
            'PERDIDAST_NT4': [
              this.values['c23_2'].values,
              this.values['c13_2'].values
            ],
            'CPROG': [
              this.values['c15_2'].values
            ],
            'CPTEP_NT1': [
              this.values['c24_2'].values
            ],
            'CPTEP_NT2': [
              this.values['c25_2'].values
            ],
            'CPTEP_NT3': [
              this.values['c26_2'].values
            ],
            'CPTEP_NT4': [
              this.values['c27_2'].values
            ]
          }
        }
        this.valoresDiferencia = false
        this.dialogFormVisible = false
        console.log('MODEL --> ', this.modelMDBCpteG)
        await postMDBCpteP(this.modelMDBCpteG, this.cpte).then(response => {
          Message({
            message: 'Registros guardados con éxito!',
            type: 'success',
            duration: 2 * 1000
          })
        })
      } else {
        Message({
          message: 'Por favor primero ingresa la novedad',
          type: 'error',
          duration: 2 * 1000
        })
      }
    }
  }
}
</script>

<style lang="scss">
	.el-collapse-item__content {
		padding-bottom: 1.5%;
	}

	.card-cpte {
		border: 2px solid #c0c4cc;
	}

	.dialog-class {
		border-radius: 10px;
	}

	.dialog-class .el-dialog__header {
		border-radius: 10px 10px 0px 0px;
	}

	// Pantallas superiores a 800px (PC)
	@media screen and (min-width: 800px) {
		.enlarge {
			border: 0px solid red;
			padding-left: 0em;
			padding-right: 0em;
		}

		.shrink {
			border: 0px solid blue;
			padding-left: 5em;
			padding-right: 5em;
		}
	}

	// Pantallas inferiores a 800px (mobile)
	@media screen and (max-width: 800px) {
		.card-cpte {
			border: 2px solid #c0c4cc;
			padding: 0 !important;
		}

		.card-cpte .el-card__body {
			padding: 0.3em !important;
		}

		.card-cpte-1 {
			border: 0px solid blue;
			padding: 0;
			margin: 0;
		}
	}
</style>
