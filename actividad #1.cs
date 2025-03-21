
using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace TrazosPerfectos
{
    public partial class FormLogin : Form
    {
        public FormLogin()
        {
            InitializeComponent();
        }

        private void btnIngresar_Click(object sender, EventArgs e)
        {
            if (txtPassword.Text == "123")
            {
                FormRegistro formRegistro = new FormRegistro();
                formRegistro.Show();
                this.Hide();
            }
            else
            {
                MessageBox.Show("Contraseña incorrecta.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }

    public partial class FormRegistro : Form
    {
        private GestionParticipantes gestion;
        public FormRegistro()
        {
            InitializeComponent();
            gestion = new GestionParticipantes();
            cmbTecnica.SelectedIndexChanged += CmbTecnica_SelectedIndexChanged;
        }

        private void CmbTecnica_SelectedIndexChanged(object sender, EventArgs e)
        {
            txtCostoClase.Text = gestion.ObtenerCostoPorTecnica(cmbTecnica.SelectedItem.ToString()).ToString();
        }

        private void btnGuardar_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrWhiteSpace(txtIdentificacion.Text) ||
                string.IsNullOrWhiteSpace(txtNombre.Text) ||
                cmbGenero.SelectedIndex == -1 ||
                cmbTecnica.SelectedIndex == -1 ||
                string.IsNullOrWhiteSpace(txtNumClases.Text))
            {
                MessageBox.Show("Todos los campos son obligatorios.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            gestion.RegistrarParticipante(new Participante(
                txtIdentificacion.Text,
                txtNombre.Text,
                cmbGenero.SelectedItem.ToString(),
                cmbTecnica.SelectedItem.ToString(),
                int.Parse(txtNumClases.Text),
                DateTime.Now
            ));
            MessageBox.Show("Registro guardado exitosamente.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void btnReporte_Click(object sender, EventArgs e)
        {
            FormReporte formReporte = new FormReporte(gestion);
            formReporte.Show();
        }
    }

    public partial class FormReporte : Form
    {
        public FormReporte(GestionParticipantes gestion)
        {
            InitializeComponent();
            lstReporte.Items.Clear();
            foreach (var p in gestion.ObtenerParticipantes())
            {
                lstReporte.Items.Add($"{p.Nombre} - {p.Tecnica} - Total: ${gestion.CalcularCostoTotal(p)}");
            }
        }
    }

    public class GestionParticipantes
    {
        private List<Participante> participantes;
        private Dictionary<string, int> preciosTecnicas = new Dictionary<string, int>
        {
            { "Dibujo", 70000 },
            { "Pintura", 85000 },
            { "Escritura", 100000 },
            { "Fotografía", 90000 },
            { "Grabado", 75000 }
        };

        public GestionParticipantes()
        {
            participantes = new List<Participante>();
        }

        public void RegistrarParticipante(Participante p)
        {
            participantes.Add(p);
        }

        public List<Participante> ObtenerParticipantes()
        {
            return participantes;
        }

        public int ObtenerCostoPorTecnica(string tecnica)
        {
            return preciosTecnicas.ContainsKey(tecnica) ? preciosTecnicas[tecnica] : 0;
        }

        public int CalcularCostoTotal(Participante p)
        {
            return p.NumeroClases * ObtenerCostoPorTecnica(p.Tecnica);
        }
    }

    public class Participante
    {
        public string Identificacion { get; }
        public string Nombre { get; }
        public string Genero { get; }
        public string Tecnica { get; }
        public int NumeroClases { get; }
        public DateTime FechaRegistro { get; }

        public Participante(string id, string nombre, string genero, string tecnica, int numClases, DateTime fecha)
        {
            Identificacion = id;
            Nombre = nombre;
            Genero = genero;
            Tecnica = tecnica;
            NumeroClases = numClases;
            FechaRegistro = fecha;
        }
    }
}


