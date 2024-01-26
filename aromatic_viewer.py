import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

# Streamlit page configuration
st.set_page_config(page_title="Aromatic Compounds Viewer")

# Title of the app
st.title("Aromatic Compounds Viewer")

# User input for multiple SMILES strings
user_input = st.text_area("Enter SMILES strings of aromatic compounds (separated by commas or new lines):", 
                          'c1ccccc1, c1ccncc1, c1cccnc1, c1ccncc1')

# Splitting the user input into individual SMILES strings
smiles_list = [smiles.strip() for smiles in user_input.replace(',', '\n').split('\n') if smiles.strip()]

# Process each SMILES string
for user_smiles in smiles_list:
    st.subheader(f"SMILES: {user_smiles}")
    
    # Convert SMILES to molecule
    molecule = Chem.MolFromSmiles(user_smiles)

    # Check if the molecule is valid
    if molecule:
        # Display the molecule
        mol_image = Draw.MolToImage(molecule)
        st.image(mol_image, use_column_width=True)
    else:
        st.error("Invalid SMILES string. Please enter a valid SMILES for an aromatic compound.")
