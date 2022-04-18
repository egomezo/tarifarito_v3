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
            <b>Componente TARIFARITO $/kWh</b>
          </span>
          <el-input v-model="cpteCalculado" type="number" style="width: 39%;" readonly />
        </el-col>
        <el-col :span="8" style="border: 0px solid yellow;">
          <span>
            <b>Componente publicado $/kWh</b>
          </span>
          <el-input v-model="cptePublicado" type="number" style="width: 39%;" readonly />
        </el-col>
        <el-col :span="8" style="border: 0px solid yellow;">
          <span>
            <b>Componente calculado revisión $/kWh</b>
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
          <el-button type="primary" class="btnVerify" @click="valoresDiferencia = !valoresDiferencia">Calcular</el-button>
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
import componentesGeneracion from './../options/componentsG'
import { getCpteGValues, postMDBCpteG } from '@/api/tarifarito/revisor/componentG'

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
      components: componentesGeneracion,
      dataParentG: null,
      input: 0,
      input1: 0,
      cptePublicado: 0,
      cpteCalculado: 0,
      valuePruebas: 0,
      values: [],
      actualiza: false,
      dataCpteG: [],
      keysValues: [],
      loadIputs: Boolean,
      dialogFormVisible: false,
      novedad: null,
      modelMDBCpteG: {},
      loading: true,
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
      this.dataParentG = JSON.parse(JSON.stringify(this.messagecomponent))
      // Se traen valores de variables
      console.log('dataParentG --> ', this.dataParentG)
      this.cptePublicado = parseFloat(
        this.dataParentG.componentes[0].component_g[0].cpte_publicado
      ).toFixed(3)
      this.cpteCalculado = parseFloat(
        this.dataParentG.componentes[0].component_g[0].cpte_calculado
      ).toFixed(3)
      if (this.dataParentG.hasOwnProperty('estado')) {
        this.modelValues = this.dataParentG.values
        // console.log('respons: ', this.modelValues)
        this.initInputs()
        this.loadInputs = true
        this.loading = false
      } else {
        await getCpteGValues(this.dataParentG).then(response => {
          this.modelValues = JSON.parse(JSON.stringify(response[0].values))
          // console.log('respons: ', this.modelValues)
          this.initInputs()
          this.loadInputs = true
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
      // console.log('FORMULA --> ', this.values)
      this.valuePruebas = 0
      // console.log('CAMPO16 --> ', parseFloat(this.values['c16_2'].values))
      const campo16 =
					parseFloat(this.values['c12_2'].values) +
					parseFloat(this.values['c13_2'].values) +
					parseFloat(this.values['c14_2'].values) +
					parseFloat(this.values['c15_2'].values)
      const campo17 = Math.min(
        1,
        (parseFloat(this.values['c1_2'].values) +
						parseFloat(this.values['c3_2'].values)) /
						campo16
      )
      const campo22 =
					(parseFloat(this.values['c4_2'].values) +
						parseFloat(this.values['c6_2'].values)) /
					(parseFloat(this.values['c1_2'].values) +
						parseFloat(this.values['c3_2'].values))
      const campo18 = 1 - campo17
      const campo23 =
					parseFloat(this.values['c8_2'].values) /
					parseFloat(this.values['c7_2'].values)
      const campo21 =
					parseFloat(this.values['c19_2'].values) +
					parseFloat(this.values['c20_2'].values)
      const campo11 =
					parseFloat(this.values['c9_2'].values) +
					parseFloat(this.values['c10_2'].values)
      const campo29 =
					campo17 *
					(parseFloat(this.values['c25_2'].values) * campo22 +
						(1 - parseFloat(this.values['c25_2'].values)) * campo11)
      const campo30 = (1 - campo17 - campo21) * campo23
      const campo28 =
					campo29 +
					campo30 +
					parseFloat(this.values['c24_2'].values) +
					parseFloat(this.values['c26_2'].values)

      this.values['c16_2'].values = campo16
      this.values['c17_2'].values = campo17
      this.values['c22_2'].values = campo22
      this.values['c18_2'].values = campo18
      this.values['c23_2'].values = campo23
      this.values['c21_2'].values = campo21
      this.values['c11_2'].values = campo11
      this.values['c29_2'].values = campo29
      this.values['c30_2'].values = campo30
      this.values['c28_2'].values = campo28

      // console.log('campo28 --> ', campo28)
      this.valuePruebas = campo28.toFixed(3)
      this.diferenciaFormula()
      // console.log('MODEL --> ', this.values)
    },
    reportar() {
      this.dialogFormVisible = true
    },
    async registrarNovedad() {
      if (this.novedad) {
        this.modelMDBCpteG = {
          usuario: this.name,
          ano: Number(this.dataParentG.ano),
          mes: Number(this.dataParentG.mes),
          cod_empresa: Number(this.dataParentG.id_empresa),
          nom_empresa: this.dataParentG.nombre_empresa,
          cod_mercado: Number(this.dataParentG.id_mercado),
          nom_mercado: this.dataParentG.mercado,
          componente: 'G',
          nt_prop: this.dataParentG.nt_prop,
          novedad: this.novedad,
          fecha_modif: moment(new Date()).format('DD/MM/YYYY HH:mm:ss'),
          estado: 'En gestión',
          componentes: [{ 'component_g': [{ 'value': 'G', 'cpte_publicado': Number(this.cptePublicado), 'cpte_calculado': this.values['c28_2'].values }] }],
          values: {
            DCR: [
              this.values['c16_2'].values,
              this.values['c12_2'].values,
              this.values['c13_2'].values,
              this.values['c14_2'].values,
              this.values['c15_2'].values
            ],
            Qc: [
              this.values['c17_2'].values
            ],
            Pc: [
              this.values['c22_2'].values,
              this.values['c1_2'].values,
              this.values['c2_2'].values,
              this.values['c3_2'].values,
              this.values['c4_2'].values,
              this.values['c5_2'].values,
              this.values['c6_2'].values
            ],
            Qb: [
              this.values['c18_2'].values
            ],
            Pb: [
              this.values['c23_2'].values,
              this.values['c7_2'].values,
              this.values['c8_2'].values
            ],
            Qagd: [
              this.values['c21_2'].values,
              this.values['c19_2'].values,
              this.values['c20_2'].values
            ],
            McAplicado: [
              this.values['c11_2'].values,
              this.values['c9_2'].values,
              this.values['c10_2'].values
            ],
            FAJ: [
              this.values['c24_2'].values
            ],
            ALFA: [
              this.values['c25_2'].values
            ],
            GTransitorio: [
              this.values['c26_2'].values
            ],
            GContratos: [
              this.values['c29_2'].values
            ],
            GBolsa: [
              this.values['c30_2'].values
            ],
            CFNC: [
              this.values['c27_2'].values
            ],
            CGeneracion: [
              this.values['c28_2'].values
            ]
          }
        }
        this.valoresDiferencia = false
        this.dialogFormVisible = false
        console.log('MODEL --> ', this.modelMDBCpteG)
        await postMDBCpteG(this.modelMDBCpteG).then(response => {
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

  .footer {
    border-top: 1px solid #c0c4cc;
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    // background-color: #f2f6fc;
    background-color: #e0f2f1;
    padding: 1em;
    // color: white;
    // text-align: center;
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
