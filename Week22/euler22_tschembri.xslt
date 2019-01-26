<!-- EULER 22 in XSLT -->
<!-- Can be tested @http://fiddle.frameless.io/ (choose Saxon-CE) -->
<!-- ~30 seconds -->

<!-- The list of names needs to be converted into an XML file with this format: -->

<!--

<names>
    <name><z>MARY</z></name>
    <name><z>PATRICIA</z></name>
    <name><z>LINDA</z></name>
    <name><z>BARBARA</z></name>
    <name><z>ELIZABETH</z></name>
    <name><z>JENNIFER</z></name>
    <name><z>MARIA</z></name>
    <name><z>SUSAN</z></name>
    .....
</names>    

-->


<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">

<xsl:template match="names">

    <!-- sort the list, the list is copied with the same structure (by the template match -->
    <!-- at the bottom) in the $sortedList variable -->
    
    <xsl:variable name="sortedList">
        <xsl:apply-templates>
            <xsl:sort select="z" />
        </xsl:apply-templates>
    </xsl:variable>
    
    <!-- each <name> node of the sorted list is processed, the template will create a -->
    <!-- <elt></elt> node for each name, the list of <elt></elt> is saved in the -->
    <!-- $individualSums variable -->
    
    <xsl:variable name="individualSums">
        <xsl:apply-templates select="$sortedList" mode="sorted" />
    </xsl:variable>
    
    <!-- the xsl return the sum of the content of each <elt></elt> node -->
    
    <xsl:value-of select="sum($individualSums/elt)" />
 
</xsl:template>
  
<!-- processes each <name></name> node -->  
  
<xsl:template match="name" mode="sorted">

    <!-- create a list of <elt></elt> for each name. Each <elt> contains the value of each letter -->
    <!-- of the name ( . - 64 = ASCII code of the letter - ASCII code of '@' (just before 'A')) -->

    <xsl:variable name="v" > 
        <xsl:for-each select="string-to-codepoints(.)">
            <xsl:element name="elt"><xsl:value-of select="( . - 64 )"/></xsl:element>
        </xsl:for-each>
    </xsl:variable>
    
    <!-- once the list is created, the template returns just an <elt></elt> -->
    <!-- which contains the sum of the value of each letter * position() which is the <name> position -->
    <!-- in the parsing ( -1 because position(1) is the root of the document ) -->
    
    <xsl:element name="elt">
        <xsl:value-of select="sum( $v / elt ) * ( position() - 1 )"/>
    </xsl:element>

</xsl:template>
  
<!-- this template returns a copy of a node -->  
  
<xsl:template match="@*|node()">
    <xsl:copy>
        <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
</xsl:template>

</xsl:stylesheet>

