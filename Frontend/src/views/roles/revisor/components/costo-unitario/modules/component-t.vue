<template>
  <div>
    <el-card ref="testDiv" :class="showCards ? 'expandir' : 'contraer'">
      <div>
        <div v-for="item in components" :key="item.key" v-loading="loading" :name="item.key">
          <el-card v-if="item.start" class="box-card margin-card">
            <div slot="header" class="clearfix">
              <span>
                <b>{{ item.title }}</b>
              </span>
            </div>
            <el-row v-if="!loading" style="font-weight: bold; padding-bottom: 1%; text-align: center;">
              <span v-for="cabecera in item.header" :key="cabecera.title">
                <el-col style="border: 0px solid red; text-align: center;" :span="cabecera.tamano">
                  <span>{{ cabecera.title }}</span>
                </el-col>
              </span>
            </el-row>
            <el-row v-if="!loading" style="border: 0px solid blue;">
              <span v-for="content in item.data" :key="content.campo">
                <el-col style="border: 0px solid;" class="contentConcept" :span="12">
                  <span class="itemText">{{ content.concepto }}</span>
                </el-col>
                <el-col style="border: 0px solid; text-align: center;" class="contentText" :span="4">
                  <span class="itemText">{{ content.unidad }}</span>
                </el-col>
                <el-col style="border: 0px solid; text-align: center;" class="contentText" :span="8">
                  <input
                    v-if="actualiza"
                    v-model="values[content.input.key].values"
                    :type="content.input.type"
                    :placeholder="content.input.placeholder"
                    :disabled="content.input.disabled"
                    style="width: 75%; height: 2em; margin-bottom: 0.5em;"
                  >
                </el-col>
              </span>
            </el-row>
          </el-card>
          <el-card
            v-else
            class="box-card margin-card"
          >
            <div slot="header" class="clearfix">
              <span>
                <b>{{ item.title }}</b>
              </span>
            </div>
            <el-row style="font-weight: bold; padding-bottom: 1%; text-align: center;">
              <span v-for="cabecera in item.header" :key="cabecera.title">
                <el-col style="border: 0px solid red; text-align: center;" :span="cabecera.tamano">
                  <span>{{ cabecera.title }}</span>
                </el-col>
              </span>
            </el-row>
            <el-row style="border: 0px solid blue;">
              <span v-for="content in item.data" :key="content.campo">
                <el-col class="contentConcept" :span="12">
                  <span class="itemText">{{ content.concepto }}</span>
                </el-col>
                <el-col style="text-align: center;" class="contentText" :span="4">
                  <span class="itemText">{{ content.unidad }}</span>
                </el-col>
                <el-col style="text-align: center;" class="contentText" :span="8">
                  <input
                    v-if="actualiza"
                    v-model="values[content.input.key].values"
                    :type="content.input.type"
                    :placeholder="content.input.placeholder"
                    :disabled="content.input.disabled"
                    style="width: 75%; height: 2em; margin-bottom: 0.5em;"
                    @input="formula()"
                  >
                </el-col>
              </span>
            </el-row>
          </el-card>
        </div>
      </div>
    </el-card>
    <div class="footer">
      <el-row :gutter="10" style="padding-right: 0em;">
        <el-col :sm="24" :md="12" class="cont-btn">
          <el-button type="primary" class="btnVerify" @click="showCards = !showCards, windowTop()">Calcular</el-button>
        </el-col>
        <el-col :sm="24" :md="12">
          <el-button v-if="!showCards" class="btn" type="success" @click="verificar">Verificado</el-button>
          <el-button v-if="showCards" class="btn" type="danger" @click="reportar">Reportar</el-button>
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
import componentesTransmision from './../options/componentsT'
import { getCpteTValues, postMDBCpteT } from '@/api/tarifarito/revisor/componentT'
export default {
  name: 'ViewT',
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
      showCards: false,
      components: componentesTransmision,
      values: [],
      actualiza: false,
      dialogFormVisible: false,
      dataParentT: null,
      novedad: null,
      cptePublicado: 0,
      cpteCalculado: 0,
      modelValues: null,
      loading: true
    }
  },
  computed: {
    ...mapGetters(['name', 'roles'])
  },
  created() {
    this.initData()
  },
  methods: {
    windowTop() {
      console.log('Namis')
      this.$refs.testDiv.scrollTop = 0
    },
    async initData() {
      // Data enviada del padre
      this.dataParentT = JSON.parse(JSON.stringify(this.messagecomponent))
      // Se traen valores de variables
      // console.log('dataParentT --> ', this.dataParentT)
      this.cptePublicado = parseFloat(
        this.dataParentT.componentes[0].component_t[0].cpte_publicado
      ).toFixed(3)
      this.cpteCalculado = parseFloat(
        this.dataParentT.componentes[0].component_t[0].cpte_calculado
      ).toFixed(3)
      if (this.dataParentT.hasOwnProperty('estado')) {
        this.modelValues = this.dataParentT.values
        console.log('respons: ', this.modelValues)
        this.initInputs()
        this.loading = false
      } else {
        await getCpteTValues(this.dataParentT).then(response => {
          this.modelValues = JSON.parse(JSON.stringify(response[0].values))
          // console.log('respons: ', this.modelValues)
          this.initInputs()
          this.loading = false
        })
      }
    },
    initInputs() {
      this.keysValues = Object.keys(this.modelValues)
      // console.log('LLAVE: ', this.keysValues)
      this.components.forEach((item, index) => {
        // console.log('ITEM: ', item)
        // console.log('ITEM_idx: ', index)
        item.data.forEach((campo, idx) => {
          // console.log('CAMPO: ', campo)
          // console.log('campo_idx: ', idx)
          const valor = this.modelValues[this.keysValues[index]][idx]
          this.values[campo.input.key] = {
            placeholder: campo.input.placeholder,
            values: valor
          }
        })
      })
      this.actualiza = true
      // this.formula()
      console.log('VALUES ->> ', this.values)
    },
    formula() {
      this.actualiza = false
      this.values['CPT'].values = parseFloat(this.values['TLAC'].values) + parseFloat(this.values['DTLAC'].values)
      this.values['CPTAGENTE'].values = parseFloat(this.values['STNAGENTE'].values) - parseFloat(this.values['CPT'].values)
      this.values['CPTLAC'].values = parseFloat(this.values['STNLAC'].values) - parseFloat(this.values['CPT'].values)
      this.actualiza = true
    },
    async registrarNovedad() {
      if (this.novedad) {
        this.modelMDBCpteT = {
          usuario: this.name,
          ano: Number(this.dataParentT.ano),
          mes: Number(this.dataParentT.mes),
          cod_empresa: Number(this.dataParentT.id_empresa),
          nom_empresa: this.dataParentT.nombre_empresa,
          cod_mercado: Number(this.dataParentT.id_mercado),
          nom_mercado: this.dataParentT.mercado,
          componente: 'T',
          nt_prop: this.dataParentT.nt_prop,
          novedad: this.novedad,
          fecha_modif: moment(new Date()).format('DD/MM/YYYY HH:mm:ss'),
          estado: 'En gestión',
          componentes: [{ 'component_t': [{ 'value': 'T', 'cpte_publicado': Number(this.cptePublicado), 'cpte_calculado': Number(this.cpteCalculado) }] }],
          values: {
            DATAPUBLICADA: [
              Number(this.cptePublicado),
              Number(this.cpteCalculado)
            ],
            CALCULOSSPD: [
              this.values['TLAC'].values,
              this.values['DTLAC'].values,
              this.values['CPT'].values
            ],
            DIFERENCIA: [
              this.values['CPTAGENTE'].values,
              this.values['CPTLAC'].values
            ]
          }
        }
        this.showCards = false
        this.dialogFormVisible = false
        console.log('MODEL --> ', this.modelMDBCpteT)
        await postMDBCpteT(this.modelMDBCpteT).then(response => {
          Message({
            message: 'Registros guardados con éxito!',
            type: 'success',
            duration: 2 * 1000
          })
          this.novedad = ''
        })
      } else {
        Message({
          message: 'Por favor primero ingresa la novedad',
          type: 'error',
          duration: 2 * 1000
        })
      }
    },
    verificar() {
      this.showCards = false
      this.$emit('clicked', false)
    },
    reportar() {
      this.dialogFormVisible = true
    }
  }
}
</script>

<style lang="scss">

	.el-collapse-item__content {
		padding-bottom: 1.5%;
	}
	.containerCards {
		border: 2px solid #c0c4cc;
		color: black;
		background-color: white;
		border-radius: 5px;
	}
	.contentConcept {
		border: 0px solid red;
		line-height: 2em;
		text-align: left;
		padding-left: 10%;
	}
	.contentText {
		border: 0px solid red;
		line-height: 3em;
		text-align: center;
	}
	.itemText {
		display: inline-block;
		vertical-align: middle;
		line-height: normal;
	}

	.expandir {
		height: 38em;
		overflow-y: scroll;
	}

	.contraer {
		height: 18em;
		overflow-y: none;
	}
</style>
